# Cyrus daily reel playbook

The daily scheduled task reads this file every morning. It makes one new reel for Instagram @cyrusdigital,
entirely in code, and schedules it for the posting time below (Europe/London).

Posting time: 09:00
(Kept at 09:00 in the 21 Nov and 25 Nov reviews: only 1 follower, so no online_followers data yet. Revisit once it is available.)

Rules changed by reviews are marked "(review 21 Nov)" or "(review 25 Nov)". LEARNINGS.md explains why. Newest rule wins.

## TODAY ONLY (27 Nov 2026, set by Mr. Abasi): NO DAILY REEL
Today's post is the hand-made Danny garage reel, already scheduled for 09:00 (Supermetrics scheduled_id 36653, see posts.md).
Mr. Abasi asked for it to replace today's daily reel. If this run is on 2026-11-27: do NOT make or post a reel, do NOT
schedule anything. Just reply that today's post is the garage reel at 09:00. From 28 Nov this section no longer applies
(delete it on the 28 Nov run).

## THE WINNING FORMAT (review 25 Nov, read this first)
The two animated character stories with a voiceover (23 and 24 Nov) beat every short text reel by a mile:
about 140 views each vs 9 to 19, skip rate about 42% vs 57 to 100%, average watch 17 to 18s vs 2 to 5s.
So the default reel is now an ANIMATED CHARACTER STORY (style 18) with an ElevenLabs voiceover and subtitles.
- About 70% of posts: style 18 character story, 35 to 60 seconds, people with faces and reactions, warm scenes,
  a fictional small business, subtitles in dark pills at the top, logo only on the end card.
- Viewers drop off around 17 to 18 seconds on both the 48s and the 70s reel. So: the problem must be clear in the
  first 3 seconds, there must be a funny turn or "oh no" moment by about 12 to 15 seconds, and a re-hook line around
  15s ("And it gets worse." / "Then it got weird.") to carry people into the second half.
- Each story uses a NEW business type and a new character (bakery is done: try a plumber, barber, salon, cafe, dentist,
  florist, mechanic, gym). Swap day and night palettes. Reuse person() from src/2026-11-24/reel.html and add new
  hair styles, clothes and props rather than redrawing from scratch.
- The short 7 to 10 second text-only reels are retired as the default. They may come back only as a labelled experiment.
- About 30% experiments, one thing at a time, inside the character format (see Content mix).

## The business
- Cyrus Digital (full trading name Cyrus Digital Solutions), run by Bardia Abasi.
- Sells: websites, apps, Google Ads management, AI receptionists and chatbots, online ordering and booking,
  Google Business Profile setup, and Google review NFC cards (from £15, a side offer, never the main sell).
- Customers: independent businesses. Restaurants, cafes, salons, barbers, shops, clinics, trades.
- NOT tied to a location. Never mention London, North London, Southgate or any area in videos, captions or hashtags.
- Main offer and call to action: a free Google check / free website check. "DM CHECK".
  (review 21 Nov) Only used on SALES posts, at most 1 post in 4. Check posts.md: if any of the last 3 posts had
  the sales CTA, today is not a sales post.
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
- Captions (review 21 Nov): 1 to 3 short lines that read like a person posting, not an ad. Vary the shape every day
  (a one-liner, a question, a tiny story, a "tag someone who..."). Non-sales posts have NO "DM CHECK" and no service
  pitch in the caption: end with a share or comment prompt instead ("send this to the owner who needs it",
  "tag your mate who says everything looks great"). Sales posts may end with the DM CHECK line.
- Hashtags (review 21 Nov): 3 to 5, and never the same set as either of the last 2 posts (check posts.md /
  src/*/caption.txt). Mix one broad tag with niche ones. No location hashtags.
  Pool: #smallbusiness #webdesign #websitedesign #googleads #localbusiness #ukbusiness #restaurantmarketing
  #salonowner #smallbusinessowner #googlereviews #digitalmarketing #businesstips #entrepreneur #smallbizlife
  #businessowner #webdesignhumor #cafeowner #barbershop #startuplife #relatable #websitetips
  #storytime #bakery #tradesman #plumber #hairsalon #animation
  (review 25 Nov) Both winners used #storytime plus one niche tag for the story's business. Keep #storytime on
  character stories for now (allowed to repeat), and vary the rest so the full set never matches the last 2 posts.
- Captions (review 25 Nov): open with the character's name and the problem in one line (both winners did this),
  then one short line, then hashtags.

## What makes these go viral
- The FIRST FRAME must already show the hook in big text (it is the cover and the scroll-stopper). No fade-in from black.
  (review 21 Nov) Skip rate was 83 to 100% on every reel, so frame 0 must ALSO have motion already under way
  (something moving, swiping or scaling from t=0, not starting at 0.5s), and the hook is max 7 words, 130px+ type.
  The first change on screen happens by 0.8s.
- (review 25 Nov) Length 35 to 60 seconds for character stories (the 21 Nov 7 to 10 second rule is retired; short
  reels held 2 to 5s, the long stories held 17 to 18s). Something changes on screen at least every 1 to 1.5 seconds.
- (review 25 Nov) First frame: the character's face mid-problem (already moving at t=0) plus the hook in big text,
  max 7 words, 130px+. Both winners opened like this.
- A payoff or twist in the middle (before vs after, a reveal, a number ticking, a "now watch this").
- Loopable ending where possible. End card for the last 2 to 2.5 seconds: logo, one line, CTA pill, @cyrusdigital.
- Content the viewer can react to: "which would you click?", "rate it out of 10", "comment your business name".
- (review 21 Nov) At most 1 in 4 posts is a sales post. The rest are content people want to share.
- End card on NON-sales posts: logo, one line, a soft CTA pill ("Follow for more", "Send this to a business owner")
  and @cyrusdigital. Sales posts use the DM "CHECK" pill.

## Content mix (review 21 Nov, updated review 25 Nov)
Format (what the reel IS) is chosen separately from visual style (how it LOOKS).
- ~70% WINNING FORMAT (review 25 Nov): animated character story with a voiceover (see "THE WINNING FORMAT" above).
  A customer or owner hits a very recognisable problem, it gets worse, a funny turn, the fix, a punchline.
  Funny, recognisable, not advice. (Before 25 Nov this slot was the short twist reel; the 16 Nov chat skit with 79 views
  was the best of those, and the character stories beat it by about 2x on views and 8x on watch time.)
- ~30% EXPERIMENTS, one new thing at a time, all inside the character format (see LEARNINGS.md "Next experiments"):
  E5 (25 Nov) Complete story in ONE reel, 30 to 40 seconds, no "part 1/2". Tests whether a shorter complete story keeps
     the ~42% skip rate and gets watch time past half the reel.
  E6 Two-part series again with a new character. Tests whether the "part 1 of 2" cliffhanger brings follows or
     return viewers (23 and 24 Nov got similar views, so the effect is unclear).
  E1 "Rate this website" told through a character reacting to a fictional bad site, asks viewers for their score.
     Tests whether an opinion question gets comments.
  E3 Comment bait ending ("comment your business type and I'll tell you the one thing to fix"). Tests comments.
  E2 Fast build timelapse (retired from the queue for now: it is a no-people format).
  Each experiment post says in posts.md "experiment: E<n> <what it tests>".
- Sales post (DM CHECK) at most 1 in 4, and it can still use the winning format.
- (23 Nov, Mr. Abasi) He wants reels to show PEOPLE (animated characters with faces and reactions) and NOT feel like ads:
  story first, subtitles of what the voice says, warm scene colours, logo only on the end card. Use the person() character
  code in src/2026-11-23/reel.html as a base (Jay, his mum, the baker; expressions, arm poses, props).
  E4 (23 Nov): long character story, 70s, part 1 of 2 ("The customer who almost paid"). Compare with the short reels at the next review.
  Part 2 posted 24 Nov ("She tried to buy her own cake", 48s, Rose the baker, sales CTA). Judge parts 1 and 2 together
  against the short reels at the next review (4 posts after the 21 Nov review = 21, 22, 23, 24 Nov, so the next run reviews).
- Safe zones on a 1080x1920 frame: keep text out of the top 200px, the bottom 380px and the right 140px.

## Style rotation
(review 25 Nov) Style 18 (animated character story) is the winning style and may be used EVERY day. Variety now comes
from the business, the characters, the setting and the palette (day vs night, warm vs cool), not from switching style.
Styles 1 to 16 below are best used as SCREENS INSIDE the story (the phone shows a search, a chat, a bad website, a
before/after) rather than as whole reels. A non-18 style is only used as a labelled experiment.
(review 21 Nov) Old rule, now only for experiments: pick a style not used in the last 5 posts.
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
15. Browser-tab drama: a fictional site in a browser window, a cursor, tabs opening and closing (light)
16. Sticky-note / receipt-paper story: each beat printed on a receipt that feeds up the screen
17. (unused number)
18. Animated character story (review 25 Nov: the winner). SVG people from person() in src/2026-11-24/reel.html,
    warm scenes, a phone that slides in for screens, subtitles in dark pills, voiceover, logo only on the end card.
Mix it up further with colour (light days and dark days), pace, and layout. Invent new styles when the list feels stale.

## Hook bank (pick one not used yet, or write a fresh one in the same spirit)
(review 21 Nov) Retired (used and flopped, advice-style): "Your website has 3 seconds.", "4.9 stars and nobody can
find you.", "Missed calls are missed customers.", "Your menu is a PDF. We need to talk.",
"Things customers won't tell you about your website.", "Your website called. It wants 2009 back."
(review 25 Nov) Winners: "He had his card out." and "She tried to buy her own cake." Both name a person and a problem
in a few words. Write new hooks in that shape: a character + a situation that is about to go wrong. Retired (short text
reels that flopped): "Everyone says your website is great.", "POV: booking you at 11pm."
New character-story hooks (use these first):
- Her kitchen's flooding. Where's his number?
- He walked in for a haircut. Walked out.
- She just wanted to book a table.
- He drove past your shop for 3 years.
- His van was full. His phone wasn't ringing.
- She left a 5 star review. Nobody saw it.
Older twist / relatable hooks:
- Plot twist: the website was the problem.
- Everyone says your website is great.
- POV: a customer tries to book you at 11pm.
- You vs your customer looking for your phone number.
- Your cousin built your website. It shows.
- The customer was ready to pay. Then this happened.
- Nobody tells you this when you open a shop.
- She drove past your shop for 3 years.
- Rate this website out of 10. Be honest. (E1)
Older bank:
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

## Voiceovers (EVERY reel, rule set by Mr. Abasi on 23 Nov 2026)
- Every reel gets an ElevenLabs voiceover. A review may tune script style, pacing and voice levels, but may not turn
  voiceovers off. The old curl pre-check and "every 2 to 3 days" rule are gone.
- The audio is NEVER downloaded into this workspace (elevenlabsusercontent.com is blocked here). The voice is generated
  and mixed into the video inside ElevenLabs, and Instagram fetches the finished video straight from ElevenLabs' link.
- Voice: "Ryan - Young, cool and confident" (voice_id 50y2RdLRjpTShM4ZFm5D), model eleven_v4, generations_count 1.
- Script: natural spoken British English, short sentences, like talking to a mate, no em dashes, no AI-sounding phrases.
  About 2.5 words per second of reel (eleven_v4 Ryan actually runs nearer 2.2 to 2.4). Tell the story in its own words,
  don't read the on-screen text out. Save it as src/DATE/vo.txt.
  (review 25 Nov) The female voice (23 Nov) and Ryan (24 Nov) did equally well, so keep Ryan. Put a re-hook line
  around the 15 second mark. Subtitles follow the voice (from silencedetect), in dark pills at the top.
- Steps (ElevenLabs connector, mcp__ElevenLabs__*):
  1. creative_create_flow "Cyrus reel DATE"; pass the flow_id to every call.
  2. creative_generate_speech with the script. Keep the generation_id (from creative_get_flow_run_status). Never call it
     twice to retry, it charges again.
  3. After about 20s, creative_execute_sandbox with the generation as /workspace/in/vo.mp3 and ffprobe it for the length.
     Silence detection in the same sandbox (ffmpeg silencedetect) gives the sentence timings to sync beats and subtitles.
  4. Build the reel to that length (at least VO + 0.8s; the voice finishes before or as the end card appears), render with
     the sfx bed, commit and push, get the SHA.
  5. creative_attach_reference_file with https://cdn.jsdelivr.net/gh/bardiaepic-hub/cyrus-reels@<SHA>/reels/DATE.mp4.
  6. creative_execute_sandbox mixing reel.mp4 + vo.mp3 (sfx bed about -16 dB under the voice, voice loudnorm -14 LUFS,
     200ms voice delay, last frame held if the voice runs long) into $OUT/reel-vo.mp4.
  7. creative_add_flow_node composition (eleven_composition) from that output, creative_run_flow_nodes, then
     creative_get_generations for full_res_url (content.mp4?Expires=...). That URL is the media_url for posting.
- Fallback: if any voice step fails after one retry, post the sfx-only jsdelivr reel and log "VO failed: <reason>".
  Never skip the day's post because of the voiceover.

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
   media_url = the ElevenLabs full_res_url (or the jsdelivr URL in the fallback), caption, timezone Europe/London,
   publish_at "DATE T<Posting time>" only if the link's Expires is 30+ min after it and it is 6+ min away, else post now,
   platform_options {"share_to_feed": true, "thumb_offset": 0}. Run with validate_only true first, then for real.
4. Before scheduling, check manage_social_media status (no ids) to make sure nothing is already scheduled for that date.
