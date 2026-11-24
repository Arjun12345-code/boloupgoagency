from PIL import Image

for name in ['boloup-header-logo.png', 'boloup-avatar-192x192.png', 'icon-only.png', 'boloup-transparent-logo.png', 'logo-samping.png']:
    im = Image.open('assets/images/' + name).convert('RGBA')
    print(f"=== {name} ({im.size}) ===")
    # find min and max RGB for non-transparent pixels
    rgbs = []
    for p in im.getdata():
        if p[3] > 100:
            r, g, b, _ = p
            if not (r < 30 and g < 30 and b < 30) and not (r > 240 and g > 240 and b > 240):
                rgbs.append((r, g, b))
    if rgbs:
        # Sort by hue or redness
        print("Sample prominent colors (hex):")
        unique_colors = list(set(rgbs))
        # sort by red descending, green ascending
        unique_colors.sort(key=lambda c: (-c[0], c[1], c[2]))
        for c in unique_colors[:8]:
            print(f"  #{c[0]:02X}{c[1]:02X}{c[2]:02X} (R={c[0]}, G={c[1]}, B={c[2]})")

