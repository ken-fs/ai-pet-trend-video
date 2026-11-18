# AI Pet Trend Video Toolkit

English | [中文](README.zh-CN.md)

Tools and notes for putting your own dog or cat into viral TikTok, Instagram Reels and YouTube Shorts pet trends: a clip-prep script, an AI-agent skill, a list of current pet trend templates, and an honest comparison of AI pet video apps.

> Made by the team behind [MyPetDance](https://mypetdance.com), one of the apps in the comparison below. The script and the skill work on their own; you don't need our site to use them.

- **[`petclip.py`](petclip.py)**: paste a TikTok / Reels / Shorts link, get the original clip at 9:16 720p, a clean 6-second version (it doesn't stop a split second into a new shot), the original sound as MP3, every camera cut with its time, and a contact sheet. It also checks your pet photos for size, format and blur before you upload them anywhere.
- **[`skills/pet-trend-video`](skills/pet-trend-video/SKILL.md)**: a skill for Claude Code, Codex and other coding agents. Ask "put my cat in the dancing kittens video" and the agent finds the original, runs `petclip`, names the sound, checks your photo and picks the quickest way to make your version.
- **[Pet trend templates](#pet-trend-templates)**: 14 current pet trends, what happens in each, the lengths, which pets work, and **[how to make each one](#how-to-make-each-pet-trend-video)**.
- **[AI pet video apps compared](#ai-pet-video-apps-compared)**, with prices from each app's own pages.

## Pet trend templates

Every pet trend that's a ready template on MyPetDance as of 16 November 2026. You upload one photo of your dog or cat and get the trend clip back with your pet in it and the original sound. Facts (dates, plays, songs) are the ones on each page, with the date they were checked there.

| Trend | What happens | Length (short / full) | Pets that work | Page |
|---|---|---|---|---|
| Left Right Dog Dance | Your dog stands in a tiled shower with a white towel on its head and sways left and right. Original by @jonnyslife_ (14 May 2026, 10.4 million plays), sound "Follow The Leader". | 6 s / 15 s | 1 dog (cats untested) | [mypetdance.com](https://mypetdance.com/) |
| It's Time Cat Meme | A kitten in a Santa hat and glowing shades yells "It's time!" on a snowy road, then two more kittens show up. From @meowtakeover, 13 November 2026. | 6 s / 10 s | 1–3 cats or dogs | [/its-time-cat-meme](https://mypetdance.com/its-time-cat-meme) |
| Pet Santa Costume | Your pet sits by a lit Christmas tree in a red Santa suit and hat, tilts its head and waves a paw while snow falls outside. | 6 s / 8 s | 1 dog or cat | [/pet-santa-costume-ai](https://mypetdance.com/pet-santa-costume-ai) |
| Cat Taxi | Your pet turns giant, runs up to the curb at night, and a man in a suit climbs on and rides it home. From @cat_vlog365 on Instagram, 10 November 2026. | 6 s / 12 s | 1 dog or cat | [/cat-taxi-ai](https://mypetdance.com/cat-taxi-ai) |
| Singing Dog | Your pet throws its head back and sings the auto-tuned singing dog song in a supermarket aisle. Its sound was in 21,665 TikTok videos by 14 November 2026. | 6 s / 13 s | 1 dog or cat | [/singing-dog-ai](https://mypetdance.com/singing-dog-ai) |
| Suave Cat Dance | Three kittens dance on wet sand by the water at night to El Alfa's "Suave". From @meowtakeover, 29 October 2026. | 6 s / 24 s | 1–2 cats (dogs work too) | [/suave-cat-dance](https://mypetdance.com/suave-cat-dance) |
| Hit the Road Dude | Your pet sits in a white pickup in a camo cap, points you off its land and says "hit the road, dude" with the meme's audio. | 6 s / 15 s | 1 dog or cat | [/hit-the-road-dude-pet](https://mypetdance.com/hit-the-road-dude-pet) |
| Dancing Pug (Dog Pool Party) | Your pet dances at a night pool party in pink goggles and arm floats. From @lucasthepuglife, 8 November 2026. | 6 s only | 1 dog or cat | [/dancing-pug-ai](https://mypetdance.com/dancing-pug-ai) |
| It's My Life Dog | Your pet drives down a highway singing Bon Jovi's "It's My Life", stares into the camera and gets sunglasses for the last line. | 6 s / 15 s | 1 dog or cat | [/its-my-life-dog-ai](https://mypetdance.com/its-my-life-dog-ai) |
| Cat Riding Surron | Your cat rides a purple Surron-style e-bike down a highway in a gold chain, front wheel up. From @ridefx__, 7 November 2026. | 6 s / 13 s | 1 cat (dogs work, only a cat tested) | [/cat-riding-surron-ai](https://mypetdance.com/cat-riding-surron-ai) |
| Kitten Parade | Your cat leads a line of kittens past a low camera on a snowy night, to "Kiat Jud Dai", and licks the lens at the end. From @memescreens, 6 November 2026. | 6 s / 13 s | 1 cat (a shiba inu worked too) | [/kitten-parade](https://mypetdance.com/kitten-parade) |
| Grinch Pet Filter | Your pet lies on a white rug by a Christmas tree; after a gold sparkle it's bright green in a Santa hat and red jacket. Our own clip with original music, not the film character. | 6 s / 9 s | 1 dog or cat | [/grinch-pet-filter](https://mypetdance.com/grinch-pet-filter) |
| Dancing Kittens | Three kittens stand on their back legs by a road at night and dance to the beat. From @meowtakeover, 29 June 2026, 108 million plays by 9 November. | 6 s / 11 s | 1–3 cats | [/kittens-dance-ai](https://mypetdance.com/kittens-dance-ai) |
| Smalltown Boy Cat | Two cats take turns screaming into the camera and dancing at a red fence, to Bronski Beat's "Smalltown Boy". | 14 s | 1–2 cats | [/smalltown-boy-cat](https://mypetdance.com/smalltown-boy-cat) |

The quick read: for one dog, start with Left Right Dog Dance, Hit the Road Dude or It's My Life Dog. For cats, Dancing Kittens and Suave Cat Dance take more than one cat. For Christmas, it's the It's Time Cat Meme, Pet Santa Costume and the Grinch Pet Filter; all three are side by side, with free GIFs to download, on [Christmas cat meme](https://mypetdance.com/christmas-cat-meme) and [Christmas dog meme](https://mypetdance.com/christmas-dog-meme).

More guides on the site: [AI dog dancing: where it came from](https://mypetdance.com/ai-dog-dancing-trend) · [How to make your dog dance with AI](https://mypetdance.com/how-to-make-your-dog-dance-ai) · [Dancing dog meme](https://mypetdance.com/dancing-dog-meme) · [Dancing cat meme](https://mypetdance.com/dancing-cat-meme) · [Christmas cat meme](https://mypetdance.com/christmas-cat-meme) · [Christmas dog meme](https://mypetdance.com/christmas-dog-meme) · [AI cat dance](https://mypetdance.com/ai-cat-dance) · [Dog dancing app](https://mypetdance.com/dog-dancing-app) · [AI dog dancing GIFs](https://mypetdance.com/ai-dog-dancing-gif) · [AI cat dance GIFs](https://mypetdance.com/ai-cat-dance-gif) · [All templates](https://mypetdance.com/templates)

## How to make each pet trend video

The steps are the same for all of them:

1. Take or pick one sharp photo of your pet facing the camera, face and ears in view, nobody else in the frame. Take off hats and costumes; the trend's outfit gets added. Not sure the photo is sharp enough? Run `python3 petclip.py photo yourpet.jpg`.
2. Open the trend's page, upload the photo and pick the short or the full version.
3. Short versions take about 8 minutes and full ones 12 to 15. You get an email when it's ready.
4. Post it with the sound that's already in the video, and turn on the platform's AI label.

What's different for each trend:

### How to make the left right dog dance video

One photo of your dog, front-on. Very fluffy dogs like a Samoyed or a Pomeranian can come out with a softer face. The 6-second version is a quick taste; the 15-second one has every sway and the turn. Make it on [the MyPetDance homepage](https://mypetdance.com/).

### How to make the It's Time cat meme with your cat

Photo 1 is the kitten in the Santa hat up front. Photos 2 and 3 are the kittens in the elf and reindeer hats at the back, which only show up from 4.5 seconds, so pick the full 10 seconds if you swap them. Cats and small dogs work best in the back spots. [Make the It's Time cat meme](https://mypetdance.com/its-time-cat-meme).

### How to make a pet Santa costume video

Your pet never wears anything: any normal photo works, and the suit and hat are added in the video. Collars and bandanas stay on if they're in the photo. The full 8 seconds finishes the tune properly, so pick it for a Christmas card. [Make the pet Santa costume video](https://mypetdance.com/pet-santa-costume-ai).

### How to make the cat taxi video with your pet

Your pet is seen from the side and the back when it runs, so a photo with the whole body in view helps. The full 12 seconds starts with the man hailing your pet like a cab; the 6-second version starts when your pet is already at the curb. [Make the cat taxi video](https://mypetdance.com/cat-taxi-ai).

### How to make the singing dog meme with your pet

It's a close-up, so the face matters more than the body. The video comes without text: add your own caption ("me when my song comes on in the car") in TikTok, Instagram or CapCut. [Make the singing dog video](https://mypetdance.com/singing-dog-ai).

### How to make the Suave cat dance with your cat

Photo 1 replaces the middle kitten with the collar, photo 2 the cream kitten on the left. The grey tabby on the right stays the original. It's a night scene, so light coats show up best. [Make the Suave cat dance](https://mypetdance.com/suave-cat-dance).

### How to make the Hit the Road Dude pet video

A photo with both ears clearly visible gives the camo cap the most natural fit. The 6-second version is just the punchline; the 15-second one adds the "this is private property" setup. [Make the Hit the Road Dude video](https://mypetdance.com/hit-the-road-dude-pet).

### How to make the dancing pug pool party video with your dog

Any dog or cat works, not only pugs. It's 6 seconds because in the rest of the original the pug turns its back, and in tests dogs turned back into the pug at that point. [Make the dancing pug video](https://mypetdance.com/dancing-pug-ai).

### How to make the It's My Life dog video

Use a photo where the eyes are open and the mouth isn't hidden: the sunglasses go over the eyes at the end, and your pet sings. The 6-second version is the stare, the sunglasses and the last line. [Make the It's My Life dog video](https://mypetdance.com/its-my-life-dog-ai).

### How to make the cat riding Surron video

No CapCut template or editing: one photo of your cat in, MP4 out. A calm, lazy-looking cat pulling a wheelie is the funniest version. [Make the cat riding Surron video](https://mypetdance.com/cat-riding-surron-ai).

### How to make the kitten parade video with your cat

Your cat leads the parade and comes back in the last second to lick the lens, so pick the full 13 seconds for the punchline. Light coats stand out best against the snow. [Make the kitten parade](https://mypetdance.com/kitten-parade).

### How to make the Grinch pet filter video

No CapCut filter needed. Your pet stays recognisable when it turns green: same face, ears and fur. Very fluffy breeds can lose some face detail once the fur is green. [Make the Grinch pet video](https://mypetdance.com/grinch-pet-filter).

### How to make the dancing kittens video with your cats

Up to 3 photos: the first replaces the middle kitten, the next two the kittens at the sides. Three cats with different coats are easier to tell apart at night than three black cats. [Make the dancing kittens video](https://mypetdance.com/kittens-dance-ai).

### How to make the Smalltown Boy cat video

Photo A screams first and dances second; photo B does the opposite. Swap the upload order to flip who screams first. [Make the Smalltown Boy cat video](https://mypetdance.com/smalltown-boy-cat).

## petclip: get a pet trend clip ready

Needs Python 3.9+, [ffmpeg](https://ffmpeg.org) and [yt-dlp](https://github.com/yt-dlp/yt-dlp). No pip packages.

```bash
brew install ffmpeg yt-dlp          # macOS; on Linux use your package manager or pip install yt-dlp
git clone https://github.com/ken-fs/ai-pet-trend-video && cd ai-pet-trend-video

python3 petclip.py prep "https://www.tiktok.com/@memescreens/video/7704821004471782663" --out kitten-parade
```

```
720x1280 13.0 s · 2 shots · cuts at 10.37 s
short version 0.0–6.0 s (1 shot, clean). Pick another with --start
crop 720x1280 at (0,0) → 720x1280. Look at kitten-parade/sheet.jpg to check your pet's ears and tail aren't cut off
wrote kitten-parade/SHOTS.md and shots.json
```

What you get in the output folder:

| File | What it is |
|---|---|
| `original.mp4` | the downloaded clip, best quality available |
| `clip.mp4` / `clip.mp3` | cropped to 9:16 at 720p, and the original sound |
| `clip-6s.mp4` / `clip-6s.mp3` | the short version |
| `sheet.jpg` | one frame every 0.5 s, to check the crop and see each move |
| `SHOTS.md` / `shots.json` | every shot with its start, end and length, plus other 6-second windows you could use ([example](examples/kitten-parade-SHOTS.md)) |

Options:

- `--window 6` (default) is the length of the short version; `--window 0` skips it. Without `--start`, petclip picks a window that doesn't open or end on less than a second of a shot, preferring the start of the clip.
- `--start 9` uses the window from 9 seconds instead. Some trends have the punchline at the end (Hit the Road Dude, It's My Life Dog), so the last 6 seconds are the better short version.
- `--ratio 16:9` (or `1:1`, `4:5`, `3:4`) when the original isn't vertical and a 9:16 crop would cut a pet off. `--x-offset` / `--y-offset` move the crop.
- `--threshold 0.25` is how big a change counts as a cut. Lower it (0.15) if a cut between two similar shots is missed.

### More commands

```bash
python3 petclip.py windows clip.mp4 --length 6     # the cleanest 6-second windows
python3 petclip.py cuts clip.mp4                   # shot list only
python3 petclip.py frames clip.mp4 --out frames    # one still per shot (storyboard, thumbnails, first frames)
python3 petclip.py photo biscuit.jpg luna.png      # are these pet photos good enough to upload?
python3 petclip.py match original.mp4 repost.mp4   # same sound? where does one start in the other?
```

`photo` checks the format (JPG, PNG or WebP), the file size (many apps stop at 10 MB), the resolution, and blur. Blur is measured on the centre of the photo, where the pet usually is, so a blurred background from portrait mode doesn't count against it. In our tests on 16 November 2026, 7 sharp pet photos (600–1200 px) scored 28–39, the same photos with a light blur 38–45 and with a heavy blur 47–50; the limit is 40. So it catches clearly blurry photos, and a slightly soft one can still pass.

```
ok    cat.jpg: 1200x797, 0.1 MB · sharp (softness 31)
check cat-blurry.jpg: 1200x1800, 0.1 MB
      - looks blurry (softness 48, limit 40): take a sharper one in good light
```

`match` compares the rhythm of two sound tracks (bass, mids and highs separately), so it still works when a repost is re-encoded or quieter. Use it to find which post is the real original, or where your 6-second cut starts in the full clip:

```
same sound: score 1.00; clip-6s.mp3 starts 7.00 s into original.mp4
```

**Links that work:** TikTok, Instagram Reels, YouTube Shorts, Facebook, X and most of the [sites yt-dlp supports](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md). Local files work too. We tested two TikTok posts and one Instagram Reel on 16 November 2026.

**If it asks you to log in:** add `--cookies-from-browser chrome` (or `firefox`, `safari`, `edge`), or `--cookies cookies.txt`.

Only download clips you're allowed to use, and credit the creator when you post.

## The pet-trend-video skill

Copy the folder into your agent's skills folder:

```bash
# Claude Code
mkdir -p ~/.claude/skills && cp -r skills/pet-trend-video ~/.claude/skills/
# Codex / other agents that read skills: copy skills/pet-trend-video wherever they load skills from
```

Then ask things like "put my dog in the Hit the Road Dude video", "what song is the kitten parade", or paste a link and say "I want my cat in this one". The skill tells the agent to find the real original, get the sound right, run `petclip`, check the pet photo, then suggest filming, CapCut, an AI template app or prompting a video model, with a short checklist before posting.

## AI pet video apps compared

Checked on each app's own pages on 16 November 2026. Prices change, so check before you buy.

| App | How it works | Free to try? | Price on its site |
|---|---|---|---|
| [MyPetDance](https://mypetdance.com/pricing) (ours) | Pick a pet trend template, upload one photo of your dog or cat (two or three on some), get the real trend clip with your pet and the original sound. 720p MP4, no watermark. | No free preview. Failed renders are refunded automatically. | Credit packs, no subscription: USD 4.99 (one 6 s clip), 9.99 (one full video), 19.99, 49.99. Credits don't expire. |
| [Pet.Video](https://pet.video/pricing) | Effects and dance videos from a pet photo, including cats, dogs and other animals. | 30 credits on sign-up, enough for one 5-second 480p video. | Subscriptions from USD 9/month billed yearly (USD 108/year) for 300 credits a month; videos from 25 credits. Credit packs last 90 days, except the Mega pack. |
| [WigglePet](https://wigglepet.app/pet-video-app-no-subscription) | iOS and Android app: your pet dances, sings, talks or vlogs, with the whole body moving. | A free image trial. | One-time credit packs or a subscription, bought in the app; the site doesn't list prices. Pack credits don't expire. |
| [MakeMeme](https://makememe.video/pricing) | Meme trend templates, some with pets (for example [Pet Taxi AI](https://makememe.video/pet-taxi-ai), which takes a photo of you and one of your pet). | No free trial on the pricing page. Each trend shows its price before you generate; failed generations are refunded. | 100 credits for USD 9.99, 300 for 26.99, 1,000 for 79.99, or a monthly plan. Pet Taxi AI, 10 s: USD 1.99 at 480p, 3.99 at 720p, 7.99 at 1080p. |
| [Jump on the Trend](https://jumponthetrend.app) | Hundreds of trend templates, with a "Starring your pet" section (81 when we checked). | A free preview with no sign-up. | One video is 100 credits: 100 credits for USD 6.99 (limited-time price, normally 9.90), 300 for 14.99. Credits never expire. |
| [ViralRemix](https://viralremix.org/pricing) | Trend meme videos, often many scenes of the same trend. | No free trial on the pricing page. Failed videos are refunded. | USD 9.90 per video, 4 for 29, 8 for 49. Auto-posting plans from USD 69/month. |
| [Viggle](https://viggle.ai/pricing) | Swap a character into a video, or animate one. Not pet-specific. | Free plan with daily credits; free videos are watermarked. | Pro USD 7.99/month (80 credits, no watermark), Live 15.99, Max 63.99, all shown as discounted from 9.99, 19.99 and 79.99. |
| [CapCut](https://www.capcut.com/pricing) | User-made templates for most pet trends: you add your own photos or clips and it builds the video. Most TikTok posts of these trends are made this way. | Free plan with free templates. | Pro USD 19.99/month or 179.99/year. |

Pick by what you want. Your pet inside the actual trend clip with its sound: MyPetDance or the template sites (MakeMeme, Jump on the Trend, ViralRemix). A free look before paying: Jump on the Trend's preview or Pet.Video's sign-up credits. Your own photos cut to the beat for free: CapCut. A phone app with many kinds of pet video: WigglePet.

## License

MIT. See [LICENSE](LICENSE). Trend clips, songs and artwork belong to their creators; this repo only contains code and text.
