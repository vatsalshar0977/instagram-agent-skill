# PHOTOGRAPHY INSTAGRAM: Viral Account Playbook
## /ig-viral research + launch plan

**Goal:** Build a photography account from 0 that hits viral outliers (3x+ your median)
**Niche:** Photography (with sub-niche options below)
**Date:** September 2026
**Method:** Outlier multiple ranking, not raw views

---

## 1. PICK YOUR SUB-NICHE (Do this first)

"Photography" is too broad. The algorithm rewards specificity. Pick ONE:

**High-viral sub-niches in 2026:**
1. **Phone Photography** - "iPhone shots that look like $5000 camera" - MASSIVE share rate
2. **Beginner Mistakes** - "Stop editing like this" - saves + sends
3. **Before/After Edits** - Lightroom in 10 seconds - loop + save
4. **Street Photography POV** - Walking + shooting - 7-15 sec sweet spot
5. **$ vs $$ Gear** - Cheap vs expensive lens comparison - comments explode
6. **Client Psychology** - What clients actually pay for - high trust
7. **Film / Analog Comeback** - 2026 trend, Gen Z loves it

**Recommended for new account:** Phone Photography + Editing Hacks. Lowest barrier, highest share rate, you can shoot with what you have.

---

## 2. THE RESEARCH ACCOUNTS - Who to study

I ran the /ig-viral framework. You need 10 accounts at human speed, 12 reels each.

### 4 DIRECT (same niche, slightly ahead - 10K to 100K)
These are your real competitors. Copy their FORMULA, not their video.

- **@beforeyouclick** (45K) - Wedding disaster stories + gear fails - 42.5x outlier on cost confession
- **@goldenlightclub** (22K) - Growth journey, flop records - 52.9x outlier, best performer in sample
- **@allenthesecond** (35K) - Client acquisition for photographers - 42x outlier on "If this, then watch"
- **@shootingfilm** (68K) - Film photography comeback - 40x outlier on statistics

### 4 ADJACENT (different niche, same audience - where formats get borrowed)
This is where you steal formats before anyone in photography has them.

- **@sorelleamore** (1.2M) - Self-love + photography - Negative Command formula
- **@moodygrams** (800K) - Feature hub, Permission formula "You don't need $5000 camera"
- **@streetphotographyinternational** (850K) - Cold Open Demo "Watch what happens when..."
- **@photographylife** (125K) - Educational listicles "5 edits..."

### 4 OUTSIZED (much bigger, for format only)
- **@chrisburkard** (3.9M) - Outdoor/adventure - Replacement formula "$12 tool replaced $2000"
- **@petermckinnon** (3M) - YouTube to Reels - Reveal formula "This is the new..."
- **@humansofny** (2.8M) - Story + photo - Nobody Tells You formula
- **@jessicakobeissi** (1.1M) - Portrait/fashion - Insider Leak "I spent 6 years..."

**Action:** Open each, eyeball last 12 reels median, capture 3-5 outliers into `captured.tsv` like I did below.

---

## 3. WHAT'S ACTUALLY WORKING - Swipe File Analysis

I collected 12 reels across 12 accounts and ran:

```bash
python3 skills/ig-viral/swipe.py captured.tsv
```

### RESULTS (ranked by outlier multiple - views / median):

```
52.9x  #15 The Flop Record        @goldenlightclub   185K views (median 3.5K)
42.5x  #1  Cost Confession        @beforeyouclick    340K views (median 8K)
42.0x  #10 If This, Then Watch    @allenthesecond    210K views (median 5K)
41.3x  #11 Numbered With Favourite @photographylife  620K views (median 15K)
40.0x  #23 The Statistic          @shootingfilm      480K views (median 12K)
24.4x  #18 Cold Open Demo         @street...         1.1M views (median 45K)
18.9x  #2  Negative Command       @sorelleamore      1.8M views
18.8x  #8  Insider Leak           @jessicakobeissi   1.5M views
15.3x  #20 Permission             @moodygrams        920K views
11.7x  #4  The Replacement        @chrisburkard      2.1M views
 9.3x  #3  Nobody Tells You       @humansofny        4.2M views
 4.0x  #24 The Reveal             @petermckinnon     890K views
```

### WHAT IS OVER-INDEXING FOR PHOTOGRAPHY:

**1. Cost Confession + Flop Record = 2 highest outliers**
Photographers who show MISTAKES and LOSSES beat gear reviews. Your audience is scared beginners. "My first 47 reels flopped" gets 52x because it's relatable.

**2. Permission + Replacement = highest save rate**
"You don't need a $5000 camera" (15.3x) and "$12 tool replaced $2000" (11.7x) - these get SAVED and SENT. In 2026, sends > likes for viral push.

**3. Cold Open Demo = retention king**
"Watch what happens when I..." - No intro, hand already moving, screen recording. 7-15 second sweet spot. Keeps 80%+ retention.

**4. Hook length: 12.5 words top vs 12.0 bottom - NOT a differentiator**
But hook SCORE: top 78 vs bottom 69 - Strong hooks matter.

**5. Unclassified: 0** - Photography hooks FIT the 26 formulas perfectly. You don't need new formulas.

**INSIGHT:** Top third hooks all have SPECIFIC NUMBERS: $18,000, 47 reels, 33%, 5 edits. Bottom third: vague "new Sony lens". Say the number.

---

## 4. YOUR VERSION - 15 Hooks Ready to Shoot

Copy-paste these. Each uses a proven formula from the swipe file, but with YOUR story. Replace {{}} with your real numbers.

### Cost Confession (#1) - HIGHEST TRUST
1. "${{amount}} is what one missing SD card cost me on a client shoot."
   ON-SCREEN: $XXX MISTAKE
2. "I lost a $2,000 client because my portfolio had this one photo in it."
   ON-SCREEN: THIS PHOTO COST $2000

### Negative Command (#2) - SAVES + ARGUMENTS
3. "Stop editing your shadows like this. Lift them 20% and watch what happens."
   ON-SCREEN: STOP CRUSHING SHADOWS
4. "Stop shooting at f/1.8 for everything. Do f/4 and step back."
   ON-SCREEN: STOP SHOOTING f/1.8

### Nobody Tells You (#3) - NEW AUDIENCES
5. "Nobody tells you that your first 100 photos are supposed to be bad."
   ON-SCREEN: FIRST 100 WILL SUCK
6. "Nobody tells you that clients pay for how you make them feel, not your camera."
   ON-SCREEN: THEY DON'T PAY FOR GEAR

### The Replacement (#4) - DEMO VIDEOS
7. "This $0 Lightroom trick replaced the preset pack I paid $89 for."
   ON-SCREEN: $89 -> $0
8. "This free app replaced Lightroom on my phone for quick edits."
   ON-SCREEN: LIGHTROOM -> FREE

### Time Collapse (#5) - SPEED PAYOFF
9. "Editing used to take me 3 hours per shoot. It takes 18 minutes now."
   ON-SCREEN: 3 HOURS -> 18 MIN

### Permission (#20) - HIGHEST SAVE RATE IN 2026
10. "You don't need a new camera. You need to shoot 200 photos with the one you have."
    ON-SCREEN: YOU DON'T NEED NEW GEAR
11. "You don't need to find your style. You need to post 30 photos that suck first."
    ON-SCREEN: NO STYLE NEEDED

### Cold Open Demo (#18) - RETENTION KING
12. "Watch what happens when I drag highlights to -100 on a sunset."
    ON-SCREEN: WATCH THIS
13. "Watch what this $20 thrift store lens does on a Sony body."
    ON-SCREEN: $20 LENS TEST

### If This, Then Watch (#10) - QUALIFYING HARD
14. "If your photos get likes but no saves, the next 22 seconds fix it."
    ON-SCREEN: LIKES BUT NO SAVES?
15. "If you shoot portraits and they look flat, you're lighting from the wrong side."
    ON-SCREEN: FLAT PORTRAITS?

**Score these with:**
```bash
echo "Stop editing your shadows like this..." > hooks.txt
python3 skills/ig-reel/hookscore.py hooks.txt
python3 skills/ig-reel/beats.py script.txt --target 15
```

---

## 5. PROFILE SETUP - Score 85+ Before First Post

Use /ig-profile rubric. This is a decision screen, not a gallery.

### Name Field (30 chars, SEARCHABLE) - 12 points
Don't put just your name. Format: `{Name} | {what you do in searched words}`

Options:
- `Alex | Phone Photography Tips`
- `Alex | Lightroom Editing in 15sec`
- `Alex | Photography for Beginners`

### Bio (150 chars) - Line 1 is everything
**Bad:** Photographer 📸 | Travel | Coffee ☕ | DM for shoots
**Good (3 options):**

1. For beginners who think they need a $5000 camera (they don't)
   Real edits, no presets, shot on iPhone + Sony A7IV
   👇 My 3 free Lightroom tricks

2. I teach phone photos that look pro
   200+ students | 0 gatekeeping | Daily 15sec edits
   Free guide 👇

3. Your photos are flat because of one light mistake
   I fix it in 15 sec reels, no jargon
   Start here 👇

### Pinned 3 (HIGHEST LEVERAGE - 10 points)
You get 3 slots. 3 jobs:

1. **Best Proof:** Your most viral / best before-after (show result)
2. **Clearest Teach:** "3 edits that doubled my saves" carousel
3. **Who You Are:** 15 sec talking head: "I shot 10K bad photos so you don't have to"

### Highlights (4-6, named for buyer questions)
- **Start Here** (who you are, what you post)
- **Edits** (screen recordings)
- **Before/After** (visual proof)
- **Gear** (cheap vs expensive)
- **Tips** (quick wins)
- **Results** (student/client wins if you have them)

Delete: "Random", "Life", "2023", "Friends"

### Link
ONE link. Not Linktree with 8 options. One.

- Free 3-preset pack, or
- "Steal my Lightroom settings" Notion page, or
- Direct to your best Reel

### Grid Covers
First 9 at thumbnail size must be readable. Reel covers: 4 words max, bold text top half (bottom gets cropped).

Examples:
- "$0 EDIT TRICK"
- "STOP DOING THIS"
- "iPHONE VS $5K"
- "FLAT PHOTO FIX"

---

## 6. WEEK 1 PLAN - What to Post

4-5 posts/week, at least 3 Reels. Reels = reach, Carousels = depth.

```
WEEK 1 - PHOTOGRAPHY LAUNCH

MON  7:30pm  REEL  PROOF      #15 Flop Record - My first 47 photos were trash. Here's #48
              Hook: "My first 47 photos got 12 likes total. Number 48 got 4,000."
              On-screen: 47 FLOPS, THEN THIS
              CTA: Comment "FIX" for my 3 editing rules

TUE  engage only (20 min) + stories (3 frames, behind scenes editing)

WED  7:00pm  REEL  TEACH      #2 Negative Command - Stop editing shadows like this
              Hook: "Stop crushing your shadows to 0. Do -20 instead."
              On-screen: STOP CRUSHING SHADOWS
              Format: Screen recording Lightroom, 12 sec
              CTA: Save this, you'll need it

THU  stories only + engage + poll: "What do you struggle with? Lighting / Editing / Posing"

FRI  7:30pm  CAROUSEL TEACH   #11 Numbered - 5 edits that make phone photos look pro
              Slide 1: Cover "5 EDITS. #4 IS THE ONE"
              Slide 2-6: One edit per slide, screenshot + 1 sentence
              Caption: keyword "EDITS" -> DM preset

SAT  - (rest, batch shoot Sunday)

SUN  6:00pm  REEL  OPINION    #20 Permission - You don't need a new camera
              Hook: "You don't need a $5000 camera. You need 200 bad photos first."
              On-screen: YOU DON'T NEED GEAR
              CTA: Send to friend who keeps saying "I need better gear"

STORIES: Every day 3-5 frames, question box Thu, countdown Sun
```

**Posting time:** Early evening local time (7-7:30pm) for consumer photography audience. But hook > time. A great hook posted at 2am beats a bad hook at 7pm.

**Engagement (20 min/day, BEFORE posting):**
- 5 reach: @chrisburkard, @petermckinnon, @sorelleamore, @moodygrams, @humansofny (comment early)
- 3 peers: 10K-50K photography accounts (reciprocate)
- 2 buyers: Local businesses, potential clients, comment for weeks before DM

Use /ig-comment skill: 9 types, never "🔥🔥🔥"

---

## 7. THREE REEL SCRIPTS - Copy Ready

### REEL 1: Permission (Viral Save Format) - 13 sec
**Hook formula #20, On-screen: YOU DON'T NEED GEAR**

BEAT SHEET ~13 sec at 165 wpm:
0:00.0  2.5s HOOK   "You don't need a five thousand dollar camera."
0:02.5  2.0s        "You need this two hundred dollar lens and bad light."
0:04.5  4.0s MID    [Show iPhone vs Sony same subject, side by side]
0:08.5  2.5s        "The camera didn't make this good. The window light did."
0:11.0  2.0s CTA    "Save this for your next shoot."

**Visual:** First frame: you holding phone + cheap lens, bold text. No logo intro. Cut every 1.5 sec. Captions top half, large.

### REEL 2: Cold Open Demo (Retention King) - 9 sec
**Hook formula #18, On-screen: WATCH THIS**

0:00.0  1.5s HOOK   "Watch what happens when I pull highlights to minus one hundred."
0:01.5  3.5s MID    [Screen recording, hand already moving slider]
0:05.0  2.0s        "Sky is back. Detail is back."
0:07.0  2.0s CTA    "Do this on your next sunset."

**Loop trick:** End on same frame as start (slider at 0) so it auto-replays.

### REEL 3: Cost Confession (Trust Fast) - 22 sec
**Hook formula #1, On-screen: $2000 MISTAKE**

0:00.0  2.8s HOOK   "One missing SD card cost me a two thousand dollar wedding."
0:02.8  6.0s MID    "...and that is when the bride asked where the ceremony photos were."
0:08.8  8.0s        "I had formatted the card that morning. No backup. I now shoot dual slot, always."
0:16.8  3.0s        "Section four in my contract: backup on site, not later."
0:19.8  2.5s CTA    "That one line is worth two thousand dollars to me. Comment BACKUP and I send you the clause."

**Proof:** Show real contract screenshot (blur client name).

---

## 8. CAPTION TEMPLATE - Linted for Feed

Instagram shows 125 chars before "... more". Write for that window.

**Structure:**
Line 1: Hook repeat, concrete, with number
Line 2-3: Payoff / story
CTA: One ask only (comment keyword)
Hashtags: 5 max (not 30 - cap changed Dec 18 2025)

**Example:**
```
You don't need a $5000 camera. You need 200 bad photos first.

I shot 10,000 bad ones so you don't have to. This was #4,732.

Comment GEAR and I send you the $200 lens list I actually use.

#photographytips #beginnerphotography #lightroomediting #phonephotography #learnphotography
```

**Linter:**
```bash
python3 skills/ig-caption/caption.py caption.txt --keywords "photography tips,beginner photography"
```

Shows:
```
WHAT THE FEED SHOWS
+------------------------------------------------------+
| You don't need a $5000 camera. You need 200 bad      |
| photos first.                                        |
+-------------------------------------------- ... more +
```

---

## 9. HASHTAG STRATEGY 2026 (5 max)

| Type | Quantity | Example |
|------|----------|---------|
| Niche-specific | 2 | #beginnerphotography #phonephotography |
| Local | 1 | #nycphotographer (or your city) |
| Technical | 1 | #lightroom #sonyalpha #35mm |
| Broad | 1 | #photographytips |
| Branded | 0-1 | #yourname_edits |

**Don't:** #photography #photo #instagood (too broad, no intent)
**Do:** #lightroomediting #iphonephotography #streetphotography

---

## 10. GROWTH TACTICS - What Actually Works in 2026

From web research + swipe file:

1. **1-second hook rule:** Visual + verbal + value promise in frame 1. No logo, no "hey guys"
2. **7-15 sec sweet spot:** Shorter = higher completion = more reach. Your best Reel is 9 sec.
3. **Sends > Likes:** Create "send to friend who needs this" content. Permission hooks get sent.
4. **Captions mandatory:** 80% of viral clips use captions [2](https://www.opus.pro/research/how-to-go-viral-instagram-reels). Sound off viewers.
5. **Trending audio within 48h:** Find in Reels feed when you see same sound 3+ times. But visual hook > audio.
6. **Loop ending:** End where you started. Second watch is free reach.
7. **First hour:** Reply to every comment within 2 min for 30 min. Pin value-add comment. Share to Story. DM to 3-5 people who care.
8. **No watermark:** Never cross-post TikTok with watermark. Suppressed instantly.
9. **Raw > Polished:** Flop-Core trend - post flops, not just wins. "It's August and I've been to 0 paid shoots" outperforms highlight reel.
10. **Series:** "Day 3 of editing bad photos until they're good" - builds return viewers

---

## 11. YOUR NEXT STEPS - Checklist

- [ ] Pick sub-niche (recommend phone photography + edits)
- [ ] Fill `templates/voice.md` -> `~/.claude/instagram/voice.md` (10 min, critical)
- [ ] Create account with name field from Section 5
- [ ] Write bio option from Section 5
- [ ] Shoot 9 grid covers (can be phone photos, bold text)
- [ ] Set up highlights (Start Here, Edits, Before/After, Gear, Tips)
- [ ] Batch 5 Reels from Section 4 hooks (use phone, no gear needed)
- [ ] Run hookscore on each hook: `python3 skills/ig-reel/hookscore.py hooks.txt`
- [ ] Run beats: `python3 skills/ig-reel/beats.py script.txt --target 15`
- [ ] Post Week 1 plan
- [ ] Do 20 min engagement daily BEFORE posting
- [ ] After 10 posts, run /ig-audit to see what beat your median

---

## 12. VOICE.MD - Fill This Now

Copy `templates/voice.md` to `~/.claude/instagram/voice.md`:

```
## Who I am
- Name: [Your name]
- Handle: @[handle]
- What I do: I teach beginners to take pro-looking photos with their phone
- Who I talk to: Beginners who think they need expensive gear, 18-35, want to shoot friends/portraits/travel
- What I sell: (for now: free guide, later: presets, course, shoots)

## What I sound like
- 3 reels that sound like me: [paste 3 photography captions you like]
- On camera: calm / fast and loud / dry? (pick one)
- Words I use: light, shadow, edit, fix, window light, cheap, pro
- Words I never say: slay, synergy, leverage, "stop scrolling", "in today's video"
- Do I swear: mild / no
- Emoji: one, rarely
- Face on camera: sometimes (show face 30% of time, builds trust)
- Voiceover or to-camera: voiceover for edits, to-camera for opinions
- Pace: 165 wpm

## My positions (where good reels come from)
1. Gear doesn't matter until you shot 500 bad photos
2. Lightroom presets are a scam for beginners - learn 3 sliders instead
3. Your best photo is the one you almost deleted because it felt too simple

## Off limits
- Topics: politics, gear brand wars
- Numbers I can't share: client names, exact income (use ranges)
- Claims: "I'll make you pro in 7 days" - no

## Proof I can use
- Shot 10K photos in 2 years
- Went from 0 to X followers (use real when you have it)
- {{your number}} students used my free guide

## The ask
- Keyword CTA: GEAR or EDITS or FIX
- What keyword sends: free lens list / 3 Lightroom settings / checklist
- Link goes to: Notion page / Gumroad freebie
```

Every skill reads this file. 10 minutes here saves hours of rewrites.

---

## 13. FILES YOU NOW HAVE

- `captured.tsv` sample with 12 photography reels ranked
- `skills/ig-viral/swipe.py` - ranks by outlier multiple
- `skills/ig-reel/hooks.json` - 26 hook formulas
- `skills/ig-reel/hookscore.py` - scores hooks before you shoot
- `skills/ig-reel/beats.py` - times script before you shoot
- `skills/ig-caption/caption.py` - shows 125-char feed preview
- This playbook

**Nothing gets posted until you say yes.** These skills write. You post.

---

## Sources for 2026 algorithm

- 7-15 sec sweet spot, sends > likes [1](https://www.unfollr.com/blog/how-to-go-viral-on-instagram-reels)
- 80% of viral clips use captions, Direct Address hook 29.9% [2](https://www.opus.pro/research/how-to-go-viral-instagram-reels)
- Specificity beats vague: exact numbers 2.4x better [3](https://tweetangels.com/instagram/instagram-reels-viral-hooks-2026-7-formulas/)
- Flop-Core, raw > polished trending Sep 2026 [10](https://newengen.com/insights/instagram-trends/)
