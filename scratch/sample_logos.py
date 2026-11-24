from PIL import Image

for name in ['boloup-logo-highres.png', 'boloup-horizontal-logo.png', 'boloup-transparent-logo.png', 'logo-samping.png']:
    try:
        im = Image.open('assets/images/' + name).convert('RGBA')
        print(f"=== {name} ===")
        w, h = im.size
        # Sample non-transparent non-white/black
        colors = []
        for x in range(0, w, 5):
            for y in range(0, h, 5):
                p = im.getpixel((x, y))
                if p[3] > 150:
                    r, g, b, _ = p
                    if not (r < 40 and g < 40 and b < 40) and not (r > 230 and g > 230 and b > 230):
                        colors.append((r, g, b))
        if colors:
            from collections import Counter
            c = Counter(colors)
            print("Top colors:")
            for col, count in c.most_common(5):
                print(f"  #{col[0]:02X}{col[1]:02X}{col[2]:02X} ({count})")
    except Exception as e:
        print(name, e)

