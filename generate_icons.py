#!/usr/bin/env python3
"""
아이콘 생성 스크립트 (192x192, 512x512 PNG)
실행: python generate_icons.py
필요: pip install Pillow
"""
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("icons", exist_ok=True)

def make_icon(size):
    img = Image.new("RGB", (size, size), color="#0a0a0a")
    draw = ImageDraw.Draw(img)

    # 배경 사각형 (accent 색)
    pad = size * 0.12
    draw.rectangle([pad, pad, size - pad, size - pad], fill="#e8ff47")

    # 텍스트: "YT"
    try:
        font_size = int(size * 0.38)
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        font = ImageFont.load_default()

    text = "YT"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), text, fill="#0a0a0a", font=font)

    path = f"icons/icon-{size}.png"
    img.save(path, "PNG")
    print(f"✅ {path} 생성 완료")

make_icon(192)
make_icon(512)
print("\n완료! icons/ 폴더를 PWA 프로젝트에 복사하세요.")
