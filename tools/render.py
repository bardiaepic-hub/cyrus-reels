# usage: python3 render.py page.html out.mp4 duration [--frames t1,t2,...]
import asyncio, sys, subprocess, os
from playwright.async_api import async_playwright
page_path, out, dur = sys.argv[1], sys.argv[2], float(sys.argv[3])
frames = None
if len(sys.argv) > 5 and sys.argv[4] == '--frames':
    frames = [float(x) for x in sys.argv[5].split(',')]
FPS = 30
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox","--force-color-profile=srgb"])
        pg = await b.new_page(viewport={"width":1080,"height":1920}, device_scale_factor=1)
        errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+os.path.abspath(page_path)); await pg.wait_for_timeout(600)
        if frames:
            for t in frames:
                await pg.evaluate(f"render({t})")
                await pg.screenshot(path=f"{out}_{t:05.2f}.jpg", type="jpeg", quality=85)
            print("errors:", errs); await b.close(); return
        tmp = out[:-4] + ".part.mp4"
        ff = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
            "-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r",str(FPS),"-movflags","+faststart",tmp], stdin=subprocess.PIPE)
        n = int(round(dur*FPS))
        for i in range(n):
            await pg.evaluate(f"render({i/FPS})")
            ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
        ff.stdin.close(); rc = ff.wait()
        await b.close()
        print("errors:", errs, "rc", rc)
        if rc == 0: os.replace(tmp, out)
asyncio.run(main())
