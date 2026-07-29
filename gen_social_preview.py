#!/usr/bin/env python3
"""Compose a 1280x640 social-preview banner: AI background + crisp text overlay."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
MX = 92

# palette
ACCENT     = (139, 124, 246)
ACCENT_BR  = (167, 139, 250)
TITLE      = (255, 255, 255)
SUB        = (198, 204, 224)
FOOT       = (150, 159, 188)
PILL_TX    = (228, 233, 245)

# ---- load AI background, crop center to 2:1, resize ----
bg = Image.open(r"d:\downloads\hallucination\generated-images\A_premium_dark_abstract_backgr_2026-07-29T02-34-07.png").convert("RGB")
bw, bh = bg.size
# cover: scale to fully cover WxH, then center-crop (no black bars)
scale = max(W / bw, H / bh)
nbw, nbh = int(round(bw * scale)), int(round(bh * scale))
bg = bg.resize((nbw, nbh))
left, top = (nbw - W) // 2, (nbh - H) // 2
bg = bg.crop((left, top, left + W, top + H)).resize((W, H))

# ---- left-side darkening scrim for text legibility ----
scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(scrim)
for x in range(W):
    a = int(230 * max(0.0, 1 - x / 880))
    sd.line([x, 0, x, H], fill=(6, 8, 22, a))
bg = Image.alpha_composite(bg.convert("RGBA"), scrim).convert("RGB")
d = ImageDraw.Draw(bg)

# ---- fonts ----
reg  = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 27)
bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 62)
kick = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
pillf= ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 25)
footf= ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 22)

# left accent bar
d.rounded_rectangle([MX - 30, 196, MX - 18, 322], radius=6, fill=ACCENT)

# kicker with a small glowing dot
d.ellipse([MX, 158, MX + 12, 170], fill=ACCENT_BR)
d.text((MX + 22, 150), "AWESOME  ·  ATLAS OF HALLUCINATION RESEARCH", font=kick, fill=ACCENT_BR)

# title
d.text((MX, 184), "Awesome Hallucination Atlas", font=bold, fill=TITLE)

# subtitle
d.text((MX, 288), "A structured, interactive atlas of hallucination research", font=reg, fill=SUB)
d.text((MX, 324), "across LLM  ·  VLM  ·  MLLM  —  1900+ papers with full-text abstracts.", font=reg, fill=SUB)

# badge pills
badges = ["1900+ Papers", "Interactive Search", "Full-text Abstracts", "LLM · VLM · MLLM"]
y0 = 432; ph = 46; padx = 22; gap = 16
x = MX
for b in badges:
    w = d.textlength(b, font=pillf)
    bw2 = int(w) + padx * 2
    d.rounded_rectangle([x, y0, x + bw2, y0 + ph], radius=23,
                        fill=(139, 124, 246, 30), outline=(167, 139, 250, 140))
    d.text((x + padx, y0 + (ph - 25) // 2), b, font=pillf, fill=(240, 243, 252))
    x += bw2 + gap

# footer
d.text((MX, 590), "github.com/GuangtaoLyu/awesome-hallucination-atlas", font=footf, fill=FOOT)

out = "D:/downloads/hallucination/social-preview.png"
bg.save(out, "PNG")
print("saved", out, bg.size)
