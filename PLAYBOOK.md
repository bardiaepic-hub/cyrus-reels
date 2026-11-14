# Cyrus daily reel playbook

The daily scheduled task reads this file every morning. It makes one new reel for Instagram @cyrusdigital,
entirely in code, and schedules it for 09:00 Europe/London.

## The business
- Cyrus Digital (full trading name Cyrus Digital Solutions), run by Bardia Abasi.
- Sells: websites, apps, Google Ads management, AI receptionists and chatbots, online ordering and booking,
  Google Business Profile setup, and Google review NFC cards (from £15, a side offer, never the main sell).
- Customers: independent businesses. Restaurants, cafes, salons, barbers, shops, clinics, trades.
- NOT tied to a location. Never mention London, North London, Southgate or any area in videos, captions or hashtags.
- Main offer and call to action: a free Google check / free website check. "DM CHECK".
- Never invent clients, testimonials, results, prices (other than cards from £15) or statistics. Example businesses
  in videos are clearly fictional (e.g. "Olive & Ember"). If a number isn't common knowledge, don't use it.

## Brand
- Colours: ink #0B0D0E / #07090A, white, turquoise #1AA6A0, bright turquoise #45D9D1, deep turquoise #0C7773.
  Other accent colours are fine inside mock-ups of client sites, but Cyrus itself is black, white and turquoise.
- Type: "Inter Display" / "Inter" (installed locally, use them; don't rely on Google Fonts loading). Heavy weights (800),
  tight letter-spacing (-0.05em) for headlines. Georgia is fine for mock restaurant sites.
- Logo: brand/icon.svg (turquoise crowned C) and brand/logo-light.svg (icon + "CYRUS DIGITAL", for dark backgrounds).
- Handle on the end card: @cyrusdigital.

## Writing rules (on-screen text and captions)
- Plain everyday words. Short. Sounds like a person, not an ad agency. No "unlock", "elevate", "game-changer", "level up".
- Never use em dashes. Use full stops, commas or brackets.
- Don't repeat the same sentence template from one day to the next.
- Captions: 2 to 4 short lines, then the CTA, then 4 to 6 hashtags. No location hashtags.
  Rotate from: #smallbusiness #webdesign #websitedesign #googleads #localbusiness #ukbusiness #restaurantmarketing
  #salonowner #smallbusinessowner #googlereviews #digitalmarketing #businesstips #entrepreneur

## What makes these go viral
- The FIRST FRAME must already show the hook in big text (it is the cover and the scroll-stopper). No fade-in from black.
- 9 to 16 seconds. Something changes on screen at least every 1 to 1.5 seconds.
- A payoff or twist in the middle (before vs after, a reveal, a number ticking, a "now watch this").
- Loopable ending where possible. End card for the last 2 to 2.5 seconds: logo, one line, CTA pill, @cyrusdigital.
- Content the viewer can react to: "which would you click?", "rate it out of 10", "comment your business name".
- Only about 1 in 5 posts should be a straight sales pitch. The rest teach, entertain or provoke.
- Safe zones on a 1080x1920 frame: keep text out of the top 200px, the bottom 380px and the right 140px.

## Style rotation (pick one NOT used in the last 5 posts, see posts.md)
1. Dark kinetic type + phone mock-up (used 15 Nov)
2. Bright white editorial: huge black type, turquoise underline swipes, lots of space
3. Fake iMessage / WhatsApp chat between a business owner and a customer
4. Google search simulation: typing a query, results dropping in, the business climbing to the top
5. Split screen before vs after website, with a wipe
6. Terminal / code typing aesthetic that "builds" a website live
7. Big colour-block list ("3 signs your website is costing you customers"), one block per beat
8. Money counter: a number ticking up showing what missed customers cost per year (simple arithmetic, labelled as an example)
9. Lock-screen notification storm (new booking, new 5 star review, new order) after "fixing" a Google listing
10. Retro web parody: "your website in 2009" (Comic Sans, hit counter) vs 2026
11. A vs B poll: two designs, "which would you click?", then the reveal
12. Map zoom with pins, one pin lighting up and getting all the taps
13. 3D review card flip and tap, phone opens a review page, stars fill
14. Big typographic quote / hot take on a black or turquoise background with one bold reveal
Mix it up further with colour (light days and dark days), pace, and layout. Invent new styles when the list feels stale.

## Hook bank (pick one not used yet, or write a fresh one in the same spirit)
- Your website has 3 seconds. (used 15 Nov)
- Which one would you click?
- 4.9 stars and nobody can find you.
- This is why your competitor is always busy.
- Missed calls are missed customers.
- Rate this website out of 10.
- POV: you finally sorted your Google listing.
- Getting reviews shouldn't be this awkward.
- Nobody reads your website. They scan it.
- Delivery apps take a cut of every order. Here's the fix.
- Your Google listing is your new shop window.
- Things customers won't tell you about your website.
- Your menu is a PDF. We need to talk.
- If your website looks like this, it's costing you.
- Comment your business name and I'll show you your new website.

## Voiceovers (every 2 to 3 days)
- If posts.md shows no voiceover in the last 2 days, try one today.
- ElevenLabs voice: "Ryan - Young, cool and confident" (voice_id 50y2RdLRjpTShM4ZFm5D), model eleven_v4.
  Script: 20 to 40 words, natural spoken British English, short sentences, no em dashes.
- Get the audio file: generate with creative_generate_speech (generations_count 1), poll creative_get_flow_run_status,
  then creative_get_generations for the full_res_url and download it with curl. Time the animation to the voiceover
  length (ffprobe), mix a quiet music/sfx bed under it (voice about 0 dB, bed about -18 dB).
- If generation is busy or fails, or the download is blocked, don't retry more than once: make a no-voiceover reel
  instead and note "VO failed: <reason>" in posts.md. Never call generate twice for the same take just to retry.

## How to build (tools/)
- Write src/<YYYY-MM-DD>/reel.html: a 1080x1920 page with a global `render(t)` function that draws the frame at time t
  (seconds) deterministically. No CSS animations or timers; everything is driven by render(t). Images: ../../brand/...
- Draw key frames first and LOOK at them (at least the first frame, the busiest frame and the end card):
  `python3 tools/render.py src/DATE/reel.html /tmp/k.mp4 DURATION --frames 0,3.5,8,13`  (writes /tmp/k.mp4_<t>.jpg)
  Fix overlaps, text overflow and anything in the unsafe zones, then render once:
  `python3 tools/render.py src/DATE/reel.html src/DATE/video.mp4 DURATION`
- Sound: write src/DATE/events.json and run `python3 tools/sfx.py src/DATE/sfx.wav DURATION src/DATE/events.json`
  (kinds: kick, tick, whoosh, chime, click, pop). Then mux:
  `ffmpeg -i video.mp4 -i sfx.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart reels/DATE.mp4`
- Check: ffprobe shows h264 1080x1920 30fps with an aac track. Keep it under 15 MB.

## How to post
1. Commit src/DATE/ and reels/DATE.mp4, append the posts.md line, push to main.
2. Get the commit SHA. Media URL: https://cdn.jsdelivr.net/gh/bardiaepic-hub/cyrus-reels@<SHA>/reels/DATE.mp4
   (raw.githubusercontent.com does NOT work: wrong content type.)
3. Supermetrics manage_social_media: action publish, ds_id IGI, account_id 17841473153686231, content_type VIDEO,
   media_url as above, caption, publish_at "DATE T09:00", timezone Europe/London,
   platform_options {"share_to_feed": true, "thumb_offset": 0}. Run with validate_only true first, then for real.
4. Before scheduling, check manage_social_media status (no ids) to make sure nothing is already scheduled for that date.
