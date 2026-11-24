from PIL import Image

for name in ['assets/images/boloup-ecosystem.png', 'assets/images/boloup-agent-role.png']:
    im = Image.open(name).convert('RGBA')
    pixels = []
    for r, g, b, a in im.getdata():
        if a > 100:
            if not (r < 30 and g < 30 and b < 30) and not (r > 240 and g > 240 and b > 240):
                pixels.append((r, g, b))
    from collections import Counter
    c = Counter(pixels)
    print(f"\n=== Top colors in {name} ===")
    for col, count in c.most_common(10):
        print(f"  #{col[0]:02x}{col[1]:02x}{col[2]:02x} - RGB({col[0]}, {col[1]}, {col[2]}) - count: {count}")

