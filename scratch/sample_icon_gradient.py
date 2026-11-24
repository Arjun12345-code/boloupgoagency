from PIL import Image

im = Image.open('assets/images/icon-only.png').convert('RGBA')
w, h = im.size
print("icon-only.png size:", w, h)
# Sample colors from top to bottom through the center of the icon
for y in range(h//6, 5*h//6, h//12):
    row_colors = [im.getpixel((x, y)) for x in range(w) if im.getpixel((x, y))[3] > 200]
    if row_colors:
        avg_r = sum(c[0] for c in row_colors) // len(row_colors)
        avg_g = sum(c[1] for c in row_colors) // len(row_colors)
        avg_b = sum(c[2] for c in row_colors) // len(row_colors)
        print(f"y={y}: avg=({avg_r}, {avg_g}, {avg_b}) -> #{avg_r:02X}{avg_g:02X}{avg_b:02X}")

