"""Builds the JSON that the Make.com webhook turns into an Instagram reel.
video_url: the job's own "video_url" if given (e.g. an ElevenLabs link), else the repo file via jsdelivr at this commit."""
import json, sys
job, sha = json.load(open(sys.argv[1])), sys.argv[2]
url = job.get("video_url") or f"https://cdn.jsdelivr.net/gh/bardiaepic-hub/cyrus-reels@{sha}/{job['video']}"
print(json.dumps({"job": sys.argv[1].split("/")[-1][:-5], "video_url": url, "caption": job.get("caption", ""),
                  "cover_offset_ms": job.get("cover_offset_ms", 1500)}))
