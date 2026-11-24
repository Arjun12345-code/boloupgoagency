from PIL import Image

for name in ['boloup-header-logo.png', 'boloup-horizontal-logo.png', 'logo-samping.png', 'cropped-boloup.png', 'boloup-app-icon.png']:
    im = Image.open('assets/images/' + name).convert('RGB')
    print(f"\nImage: {name} ({im.size})")
    # Sample corner, top-left of shape, center of shape, bottom-right of shape
    # Let's find bounding box of colorful pixels
    pixels = []
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = im.getpixel((x, y))
            if r > 50 or g > 50 or b > 50:
                if not (r > 230 and g > 230 and b > 230):
                    pixels.append((x, y, r, g, b))
    if pixels:
        min_x = min(p[0] for p in pixels)
        max_x = max(p[0] for p in pixels)
        min_y = min(p[1] for p in pixels)
        max_y = max(p[1] for p in pixels)
        print(f"  Color bounding box: ({min_x}, {min_y}) to ({max_x}, {max_y})")
        # Sample left, center, right of colored region
        y_mid = (min_y + max_y) // 2
        p_left = im.getpixel((min_x + 5, y_mid))
        p_mid = im.getpixel(((min_x + max_x) // 2, y_mid))
        p_right = im.getpixel((max_x - 5, y_mid))
        print(f"  Left pixel:   RGB{p_left} -> #{p_left[0]:02x}{p_left[1]:02x}{p_left[2]:02x}")
        print(f"  Center pixel: RGB{p_mid} -> #{p_mid[0]:02x}{p_mid[1]:02x}{p_mid[2]:02x}")
        print(f"  Right pixel:  RGB{p_right} -> #{p_right[0]:02x}{p_right[1]:02x}{p_right[2]:02x}")

