from PIL import Image
from collections import Counter

for path in ['assets/images/boloup-avatar-192x192.png', 'assets/images/boloup-header-logo.png', 'assets/images/icon-only.png']:
    try:
        im = Image.open(path).convert('RGBA')
        print(f"=== {path} ({im.size}) ===")
        non_transparent = []
        for p in im.getdata():
            if p[3] > 100:
                r, g, b, _ = p
                if not (r < 30 and g < 30 and b < 30) and not (r > 240 and g > 240 and b > 240):
                    non_transparent.append((r, g, b))
        c = Counter(non_transparent)
        print("Top 10 colors:")
        for color, count in c.most_common(10):
            print(f"  RGB: {color} -> #{color[0]:02X}{color[1]:02X}{color[2]:02X} (count: {count})")
    except Exception as e:
        print(path, "error:", e)
