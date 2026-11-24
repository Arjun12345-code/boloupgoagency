from PIL import Image

def analyze_icon(path):
    im = Image.open(path).convert('RGBA')
    print(f"\n=== Analyzing {path} ===")
    # Find all non-black, non-transparent pixels
    pixels = []
    for r, g, b, a in im.getdata():
        if a > 100:
            # exclude dark background
            if not (r < 30 and g < 30 and b < 30):
                pixels.append((r, g, b))
    if not pixels:
        print("No pixels found")
        return
    from collections import Counter
    c = Counter(pixels)
    print("Top 15 colors:")
    for col, count in c.most_common(15):
        print(f"  #{col[0]:02x}{col[1]:02x}{col[2]:02x} - RGB({col[0]}, {col[1]}, {col[2]}) - count: {count}")

analyze_icon('assets/images/cropped-boloup.png')
analyze_icon('assets/images/boloup-app-icon.png')
analyze_icon('assets/images/boloup-1366.png')
analyze_icon('assets/images/icon-only.png')

