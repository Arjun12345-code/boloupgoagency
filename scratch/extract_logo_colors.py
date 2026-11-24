import os
from PIL import Image

def extract_palette(image_path, num_colors=10):
    im = Image.open(image_path)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    
    # Filter out transparent or near-black/near-white pixels
    pixels = []
    for r, g, b, a in im.getdata():
        if a > 50:
            # ignore background pure black/very dark
            if not (r < 25 and g < 25 and b < 25) and not (r > 245 and g > 245 and b > 245):
                pixels.append((r, g, b))
                
    if not pixels:
        print(f"{image_path}: No colored pixels found")
        return

    # Count frequencies
    from collections import Counter
    counts = Counter(pixels)
    most_common = counts.most_common(num_colors)
    print(f"\n=== Top Colors in {os.path.basename(image_path)} ===")
    for (r, g, b), count in most_common:
        hex_code = f"#{r:02x}{g:02x}{b:02x}"
        print(f"  {hex_code} (RGB {r}, {g}, {b}) - count: {count}")

for img in [
    'assets/images/logo-samping.png',
    'assets/images/boloup-logo-highres.png',
    'assets/images/boloup-app-icon.png',
    'assets/images/boloup-header-logo.png',
    'assets/images/bolo-perfect.png',
    'assets/images/boloup-horizontal-logo.png'
]:
    if os.path.exists(img):
        extract_palette(img, 8)

