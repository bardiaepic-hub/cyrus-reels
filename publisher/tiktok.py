"""TikTok helper for the Cyrus reels pipeline (runs inside GitHub Actions).

Tokens never sit in the repo in plain text. The refresh token is stored in
state/tiktok.enc, encrypted with the app's client secret (a GitHub secret),
and is re-saved every time TikTok hands back a new one.

Usage:
  python publisher/tiktok.py auth <url-or-code>     exchange a login code for tokens
  python publisher/tiktok.py draft <video.mp4>     send a video to the TikTok inbox as a draft
"""
import json, os, subprocess, sys, time, urllib.parse, urllib.request

API = "https://open.tiktokapis.com/v2"
KEY = os.environ["TIKTOK_CLIENT_KEY"]
SECRET = os.environ["TIKTOK_CLIENT_SECRET"]
REDIRECT = os.environ.get("TIKTOK_REDIRECT_URI", "https://cyrusdigital.co.uk/tiktok-callback")
STATE = os.path.join(os.path.dirname(__file__), "..", "state", "tiktok.enc")


def _openssl(args, data):
    p = subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-iter", "200000", "-a", "-A", *args,
                        "-pass", "env:TIKTOK_CLIENT_SECRET"], input=data, capture_output=True, check=True)
    return p.stdout


def save_tokens(tok):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    keep = {k: tok.get(k) for k in ("refresh_token", "open_id", "scope")}
    keep["saved_at"] = int(time.time())
    with open(STATE, "wb") as f:
        f.write(_openssl([], json.dumps(keep).encode()))


def load_tokens():
    with open(STATE, "rb") as f:
        return json.loads(_openssl(["-d"], f.read()))


def _post(url, data=None, form=None, token=None, method="POST"):
    headers = {}
    if form is not None:
        body = urllib.parse.urlencode(form).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    else:
        body = json.dumps(data or {}).encode()
        headers["Content-Type"] = "application/json; charset=UTF-8"
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"TikTok error {e.code}: {e.read().decode()[:500]}")


def auth(code_or_url):
    code = code_or_url.strip()
    if code.startswith("http"):
        code = urllib.parse.parse_qs(urllib.parse.urlparse(code).query)["code"][0]
    else:
        code = urllib.parse.unquote(code)
    tok = _post(API + "/oauth/token/", form={
        "client_key": KEY, "client_secret": SECRET, "code": code,
        "grant_type": "authorization_code", "redirect_uri": REDIRECT})
    if "refresh_token" not in tok:
        raise SystemExit("No token returned: " + json.dumps({k: v for k, v in tok.items() if "token" not in k}))
    save_tokens(tok)
    print("Connected TikTok account, scopes:", tok.get("scope"))


def access_token():
    saved = load_tokens()
    tok = _post(API + "/oauth/token/", form={
        "client_key": KEY, "client_secret": SECRET,
        "grant_type": "refresh_token", "refresh_token": saved["refresh_token"]})
    if "access_token" not in tok:
        raise SystemExit("Refresh failed: " + json.dumps({k: v for k, v in tok.items() if "token" not in k}))
    if tok.get("refresh_token") and tok["refresh_token"] != saved["refresh_token"]:
        save_tokens(tok)
    return tok["access_token"]


def draft(path):
    token = access_token()
    size = os.path.getsize(path)
    init = _post(API + "/post/publish/inbox/video/init/", token=token, data={
        "source_info": {"source": "FILE_UPLOAD", "video_size": size, "chunk_size": size, "total_chunk_count": 1}})
    if init.get("error", {}).get("code") not in (None, "ok"):
        raise SystemExit("Init failed: " + json.dumps(init["error"]))
    pid, up = init["data"]["publish_id"], init["data"]["upload_url"]
    with open(path, "rb") as f:
        req = urllib.request.Request(up, data=f.read(), method="PUT", headers={
            "Content-Type": "video/mp4", "Content-Length": str(size),
            "Content-Range": f"bytes 0-{size - 1}/{size}"})
        urllib.request.urlopen(req, timeout=300).read()
    status = "PROCESSING_UPLOAD"
    for _ in range(30):
        time.sleep(5)
        st = _post(API + "/post/publish/status/fetch/", token=token, data={"publish_id": pid})
        status = st.get("data", {}).get("status", status)
        if status in ("SEND_TO_USER_INBOX", "PUBLISH_COMPLETE", "FAILED"):
            if status == "FAILED":
                raise SystemExit("TikTok upload failed: " + json.dumps(st.get("data")))
            break
    print(json.dumps({"publish_id": pid, "status": status}))
    return {"publish_id": pid, "status": status}


if __name__ == "__main__":
    cmd, arg = sys.argv[1], sys.argv[2]
    if cmd == "auth":
        auth(arg)
    elif cmd == "draft":
        draft(arg)
