# REEL FORMATS — Portfolio Bird Account

Four formats. That's the whole system. No talking. No tutorials. No gear talk on camera.

**Universal rules:**
- Frame 1 must pass the Frame-1 Test (motion · one subject · sharp eye · negative space · fills 9:16 · sound exists)
- 9:16, no letterbox, no watermark, no borders
- Ambient audio only — wings, water, wind, shutter, dawn chorus. Music only if it's very low and very slow.
- Text: short, top half or bottom third, never over the bird's face
- Cut on movement, not on a count
- End on black or on the still frame, so the last thing they see is the photograph

---

## FORMAT A — THE SINGLE FRAME · 8–12 sec · 60% of your posts

**What it is:** a photograph that behaves like a Reel.

```
0.0–0.5s   0.5s of the live moment (wing twitch, head turn, water drop)
0.5–3.0s   CUT to the still, slow push-in (4%)
3.0–7.0s   Hold on the eye. Nothing else moves.
7.0–8.0s   Optional: tiny second detail crop (the feather, the water)
8.0–9.0s   Fade to black. Text appears.
```

**Text:** one line. `4 HOURS · 1 FRAME` · `SOUND ON` · `SHE CAME BACK AT DUSK`
**Audio:** ambient from the actual moment. Your shutter firing is part of the soundtrack.
**Cover:** the still frame, text in the top half.

**Why it works:** Reels get reach, stills build identity. This is both, and it takes 10 minutes to make.

---

## FORMAT B — THE SEQUENCE · 10–15 sec · 20%

**What it is:** the actual burst, unedited order. Bird lands, turns, takes off.

```
0.0–1.0s   Bird settles on the perch (or the water is calm)
1.0–6.0s   Stillness. A head turn.
6.0–8.0s   Pre-flight cue — the weight shift
8.0–11.0s  TAKEOFF. Cut hard on each wingbeat. This is the payoff.
11.0–13.0s Slow-mo on the best two frames (0.5x speed ramp)
13.0–15.0s Freeze on the final still, fade
```

**Text:** EXIF as aesthetic, not teaching. `1/2000 · THOL · 6:12 AM`
**Audio:** wingbeats. Do not put music over wingbeats.
**How to shoot it:** **RAW burst mode, 30 fps with 0.5s pre-capture** on the R8. Half-press to start buffering, full-press when the moment happens — you get the frames from before you pressed. This is the most useful feature on your body for takeoff and dive shots.

**Why it works:** sequences prove you were there, and they're the only format where 40 fps/rolling shutter doesn't matter — motion sells it.

---

## FORMAT C — THE WAIT · 20–30 sec · 10%

**What it is:** cinematic B-roll of the whole morning, ending on one frame.

```
0–4s       Dark. Hide going up. Breath in cold air. Headlamp.
4–9s       First light on the water. Nothing has happened.
9–15s      Empty branch. Long hold. (This is the point — let it be boring.)
15–20s     A distant call. Then the bird arrives.
20–26s     Two or three frames of the bird, unhurried.
26–30s     The still. Hold. Fade to black.
```

**Text:** minimal. Maybe just `SOUND ON` and a time stamp at the end.
**Audio:** dawn chorus, no music. This is your best sound asset — protect it.
**Where you appear:** here, and only here. A hand, a silhouette, a shoulder. Never a talking head.

**Why it works:** this is the piece that converts a scroller into a follower, and eventually into a print buyer. It sells patience, and patience is what you're actually selling.

---

## FORMAT D — THE SERIES CAROUSEL · 5–8 slides · every other week

**What it is:** one morning, or one species, as a set.

- **Slide 1 (cover):** strongest frame + 4 words max, top half. `ONE MORNING AT THOL`
- **Slides 2–7:** the rest of the set, in the order it happened. Vary: wide, portrait, detail, action.
- **Slide 8 (optional):** the record shot you'd never post alone — a wide of the habitat, or the empty branch. Context sells the set.
- **Caption:** one short paragraph about the morning. Species, place, time. Optional prints line.

**Why it works:** carousels are the save engine. Saves signal quality harder than likes, and they reach non-followers.

---

## PRE-POST CHECKLIST

- [ ] Frame 1 moves
- [ ] Eye is sharp at 100%
- [ ] Ambient audio present, levels not clipping
- [ ] Text doesn't sit on the bird
- [ ] No watermark, no borders, no logo
- [ ] 9:16, fills screen
- [ ] Ends on black or on the still
- [ ] Caption: atmosphere → fact → optional prints line
- [ ] 5 hashtags + feature-account tags in the first comment
- [ ] Caption linter run (see playbook §9)

## TOOLS
```bash
# hookscore is for spoken, direct-address hooks — it will underrate these. Use the Frame-1 Test.
python3 /home/user/instagram-agent-skill/skills/ig-reel/hookscore.py hooks-portfolio-bird.txt

# still useful for the few posts where you do write a spoken line
python3 /home/user/instagram-agent-skill/skills/ig-reel/beats.py script.txt --target 12 --wpm 150

python3 /home/user/instagram-agent-skill/skills/ig-caption/caption.py caption.txt --keywords "bird photography prints"
```
