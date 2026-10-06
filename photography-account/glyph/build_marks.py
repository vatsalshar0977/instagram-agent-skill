#!/usr/bin/env python3
"""
Six monogram concepts that combine VATSAL SHARMA's initials with a bird.
    python3 build_marks.py
Outputs: profile-ready 640px PNGs, transparent white masters, 32px legibility
tests, and a PDF contact sheet.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

SLATE = (22, 35, 42)
SAND = (217, 199, 167)
SAGE = (124, 139, 132)
EMBER = (201, 123, 60)
BONE = (242, 235, 224)

FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
FONT_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

SS = 4  # supersample


# ------------------------------------------------------------------ primitives
def cr_spline(pts, per=40):
    """Catmull-Rom through pts -> dense polyline."""
    p = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(len(p) - 3):
        p0, p1, p2, p3 = p[i], p[i + 1], p[i + 2], p[i + 3]
        for j in range(per):
            t = j / per
            t2, t3 = t * t, t * t * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t +
                       (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                       (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t +
                       (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                       (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    out.append(p[-2])
    return out


def stroke(d, pts, w, color):
    w = max(1.0, w)
    if len(pts) >= 2:
        d.line(pts, fill=color + (255,), width=int(round(w)), joint="curve")
    r = w / 2.0
    for (x, y) in (pts[0], pts[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill=color + (255,))


def chevron(cx, cy_apex, halfw, h, bow=0.0):
    """Bird / V shape. apex at (cx, cy_apex), tips up-left and up-right."""
    apex = (cx, cy_apex)
    lt = (cx - halfw, cy_apex - h)
    rt = (cx + halfw, cy_apex - h)
    if bow <= 0:
        return [lt, apex, rt]
    # bowed = wings: control point lifts the mid-arms
    n = 24
    left, right = [], []
    for i in range(n + 1):
        t = i / n
        mx = cx - halfw * (1 - t)
        my = cy_apex - h * (1 - t)
        lift = bow * h * math.sin(math.pi * t)
        left.append((mx, my - lift))
        mx = cx + halfw * (1 - t)
        right.append((mx, my - lift))
    return left + [apex] + right[::-1]


def s_spine(box):
    """S-curve spine inside a normalised box (x0,y0,x1,y1)."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    pts = [(0.92, 0.06), (0.55, 0.02), (0.15, 0.13), (0.03, 0.34),
           (0.42, 0.52), (0.86, 0.68), (0.80, 0.95), (0.22, 0.97)]
    return [(x0 + px * w, y0 + py * h) for px, py in cr_spline(pts)]


def ink(color):
    return color + (255,) if isinstance(color, tuple) else color


def bird_body(d, cx, cy, s, color, face=1):
    color = ink(color)
    """Minimal perched-bird silhouette, `s` = body length."""
    bw, bh = s * 0.52, s * 0.36
    d.ellipse([cx - bw, cy - bh, cx + bw, cy + bh], fill=color)
    hx = cx + face * bw * 0.86
    hy = cy - bh * 0.92
    hr = bh * 0.62
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=color)
    bl = s * 0.30
    d.polygon([(hx + face * hr * 0.72, hy - hr * 0.18),
               (hx + face * (hr * 0.72 + bl), hy + hr * 0.16),
               (hx + face * hr * 0.62, hy + hr * 0.72)], fill=color)
    tl = s * 0.46
    d.polygon([(cx - bw * 0.86, cy - bh * 0.10),
               (cx - bw * 0.86 - tl, cy - bh * 0.55),
               (cx - bw * 0.86 - tl * 0.92, cy + bh * 0.42)], fill=color)
    for dx in (-0.18, 0.14):
        lx = cx + bw * dx
        d.line([(lx, cy + bh * 0.9), (lx - s * 0.02, cy + bh * 1.75)],
               fill=color, width=max(1, int(s * 0.045)))


# ------------------------------------------------------------------ the six marks
def m_vflock(d, U, color):
    """1. V-Flock — the V is the lead bird; two smaller chevrons trail behind."""
    sw = U * 0.068
    stroke(d, [(x * U, y * U) for x, y in chevron(0.30, 0.80, 0.22, 0.30)],
           sw, color)                                        # lead = the V
    stroke(d, [(x * U, y * U) for x, y in chevron(0.62, 0.50, 0.155, 0.21, bow=0.10)],
           sw * 0.80, color)
    stroke(d, [(x * U, y * U) for x, y in chevron(0.86, 0.26, 0.105, 0.14, bow=0.12)],
           sw * 0.64, color)


def m_swan(d, U, color):
    """2. Swan-Neck S — the S becomes a heron's neck; a V rides the body as a wing."""
    sw = U * 0.085
    spine = s_spine((0.20 * U, 0.16 * U, 0.66 * U, 0.90 * U))
    stroke(d, spine, sw, color)
    hx, hy = spine[0]
    hr = sw * 0.95
    d.ellipse([hx - hr, hy - hr, hx + hr, hy + hr], fill=color)
    bl = U * 0.17
    d.polygon([(hx + hr * 0.6, hy - hr * 0.2), (hx + hr * 0.6 + bl, hy + hr * 0.1),
               (hx + hr * 0.5, hy + hr * 0.8)], fill=color + (255,))
    stroke(d, [(x * U, y * U) for x, y in chevron(0.66, 0.60, 0.20, 0.26, bow=0.08)],
           sw * 0.80, color)              # the V as a folded wing


def m_perched(d, U, color):
    """3. Perched V — a bold V as the branch, a bird standing on its right arm."""
    sw = U * 0.105
    stroke(d, [(x * U, y * U) for x, y in chevron(0.50, 0.90, 0.44, 0.58, bow=-0.0)],
           sw, color)
    bird_body(d, 0.70 * U, 0.20 * U, U * 0.34, color, face=1)


def m_wingedvs(d, U, color):
    """4. Winged VS — V is the spread wings, S is the body and tail. One bird."""
    sw = U * 0.085
    stroke(d, [(x * U, y * U) for x, y in chevron(0.50, 0.44, 0.44, 0.34, bow=0.14)],
           sw, color)                                        # wings = V
    stroke(d, s_spine((0.30 * U, 0.44 * U, 0.70 * U, 0.92 * U)), sw * 0.92, color)


def m_vstail(d, U, color, font_path=FONT_SERIF_B):
    """5. VS + Flyway — serif VS monogram, the flyway trail streams off the S."""
    f = ImageFont.truetype(font_path, int(U * 0.62))
    tmp = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    tb = tmp.textbbox((0, 0), "VS", font=f)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    x = (U - tw) / 2 - tb[0]
    y = (U * 0.86 - th) / 2 - tb[1]
    d.text((x, y), "VS", font=f, fill=color + (255,))
    sw = U * 0.055
    ox, oy = x + tw + U * 0.015, y + th * 0.30
    for i in range(3):                                        # the flyway trail
        sx = ox + i * U * 0.085
        sy = oy - i * U * 0.048
        stroke(d, [(sx, sy), (sx + U * 0.20, sy - U * 0.078)], sw * (1 - i * 0.10), color)


def m_negative(d, U, color, bg):
    """6. Negative Space — bird silhouette with VS knocked out of it."""
    sil = Image.new("L", (U * SS, U * SS), 0)
    sd = ImageDraw.Draw(sil)
    bird_body(sd, 0.52 * U * SS, 0.50 * U * SS, U * 0.92 * SS, 255, face=1)
    f = ImageFont.truetype(FONT_SANS_B, int(U * 0.30 * SS))
    tb = sd.textbbox((0, 0), "VS", font=f)
    sd.text((0.50 * U * SS - (tb[2] - tb[0]) / 2 - tb[0],
             0.52 * U * SS - (tb[3] - tb[1]) / 2 - tb[1]), "VS", font=f, fill=0)
    sil = sil.resize((U, U), Image.LANCZOS)
    mask = sil.point(lambda v: 255 if v > 110 else 0)
    layer = Image.new("RGBA", (U, U), color + (255,))
    d._image.paste(layer, (0, 0), mask)


MARKS = [
    ("1-vflock", "V-Flock", m_vflock, "The V is the lead bird. Two smaller chevrons trail behind it, so the letter and the flock are the same three strokes."),
    ("2-swan", "Swan-Neck S", m_swan, "The S stretches into a heron's neck, head and beak. A V rides the body as a folded wing. Reads VS and reads bird at once."),
    ("3-perched", "Perched V", m_perched, "A heavy V becomes the branch and a bird stands on its right arm. Most literal of the six: you see a V and you see a bird."),
    ("4-wingedvs", "Winged VS", m_wingedvs, "V is the spread wings, S is the body and tail. One bird, two letters, no text."),
    ("5-vstail", "VS + Flyway", m_vstail, "Serif VS monogram with the flyway trail streaming off the S as tail feathers. Ties straight into the glyph already built."),
    ("6-negative", "Negative Space", m_negative, "Bird silhouette with VS knocked out of the body. Boldest at large sizes, weakest at avatar size."),
]


def render(fn, size, color, bg=None, font_path=FONT_SERIF_B):
    U = size * SS
    img = Image.new("RGBA", (U, U), (bg + (255,)) if bg else (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    import inspect
    params = inspect.signature(fn).parameters
    kw = {}
    if "font_path" in params:
        kw["font_path"] = font_path
    if "bg" in params:
        kw["bg"] = bg
    fn(d, U, color, **kw)
    return img.resize((size, size), Image.LANCZOS)


made = {}
for key, name, fn, desc in MARKS:
    render(fn, 640, BONE, bg=SLATE).save(OUT / f"mark-{key}-profile-640.png")
    render(fn, 512, (255, 255, 255)).save(OUT / f"mark-{key}-white.png")
    render(fn, 512, (0, 0, 0)).save(OUT / f"mark-{key}-black.png")
    render(fn, 32, BONE, bg=SLATE).save(OUT / f"mark-{key}-32px.png")
    render(fn, 110, BONE, bg=SLATE).save(OUT / f"mark-{key}-110px.png")
    made[key] = name

# ------------------------------------------------------------------ contact sheet
pdfmetrics.registerFont(TTFont("Body", FONT_SANS))
pdfmetrics.registerFont(TTFont("Body-Bold", FONT_SANS_B))
pdfmetrics.registerFont(TTFont("Display", FONT_SERIF))

sheet = OUT / "Monogram-Concepts.pdf"
c = canvas.Canvas(str(sheet), pagesize=A4)
W, H = A4
c.setFillColorRGB(*[v / 255 for v in SLATE])
c.rect(0, H - 46, W, 46, stroke=0, fill=1)
c.setFillColorRGB(*[v / 255 for v in BONE])
c.setFont("Display", 17)
c.drawString(20 * mm, H - 30, "Vatsal Sharma — six monogram concepts")
c.setFont("Body", 8.5)
c.setFillColorRGB(*[v / 255 for v in SAND])
c.drawString(20 * mm, H - 40, "Letters from the name, combined with a bird. Bone on Slate, shown at 640px.")

y = H - 66
for key, name, fn, desc in MARKS:
    if y < 92 * mm:
        c.showPage()
        y = H - 40
    p = OUT / f"mark-{key}-profile-640.png"
    c.drawImage(str(p), 20 * mm, y - 40 * mm, width=40 * mm, height=40 * mm)
    c.drawImage(str(OUT / f"mark-{key}-32px.png"), 20 * mm + 40 * mm + 3 * mm,
                y - 40 * mm, width=6 * mm, height=6 * mm)
    c.setFillColorRGB(*[v / 255 for v in SLATE])
    c.setFont("Display", 12.5)
    c.drawString(74 * mm, y - 8 * mm, name)
    c.setFont("Body", 8.6)
    c.setFillColorRGB(*[v / 255 for v in (60, 74, 81)])
    words, line = desc.split(), ""
    ly = y - 15 * mm
    for w in words:
        if c.stringWidth(line + " " + w, "Body", 8.6) > 108 * mm:
            c.drawString(74 * mm, ly, line)
            ly -= 4.6 * mm
            line = w
        else:
            line = (line + " " + w).strip()
    c.drawString(74 * mm, ly, line)
    c.setFillColorRGB(*[v / 255 for v in (140, 150, 145)])
    c.setFont("Body", 7.5)
    c.drawString(20 * mm, y - 44 * mm, f"mark-{key}-profile-640.png   ·   -white.png   ·   -black.png   ·   -32px.png")
    y -= 56 * mm

c.setFillColorRGB(*[v / 255 for v in SAGE])
c.setFont("Body", 7.5)
c.drawString(20 * mm, 12 * mm,
             "Vatsal Sharma · monogram concepts · Slate #16232A · Sand #D9C7A7 · Ember #C97B3C · Bone #F2EBE0")
c.showPage()
c.save()

print("Built", len(MARKS), "concepts:")
for f in sorted(OUT.glob("mark-*")):
    print(f"  {f.name:38s} {f.stat().st_size:>7,} B")
print("  Monogram-Concepts.pdf")
