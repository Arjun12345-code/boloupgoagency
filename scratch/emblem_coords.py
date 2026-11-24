from PIL import Image

im = Image.open('assets/images/cropped-boloup.png').convert('RGB')
colors = []
for y in range(0, im.height, 5):
    for x in range(0, im.width, 5):
        r, g, b = im.getpixel((x, y))
        if r > 40 or g > 40 or b > 40:
            if not (r < 30 and g < 30 and b < 30):
                colors.append((x, y, r, g, b))

# Calculate average (x, y) for purple, pink, orange
purple = [(x, y) for (x, y, r, g, b) in colors if b > 140 and r < 180]
pink = [(x, y) for (x, y, r, g, b) in colors if r > 200 and b > 100]
orange = [(x, y) for (x, y, r, g, b) in colors if r > 200 and g > 70 and b < 70]

def avg(lst):
    return (sum(x for x, y in lst) // len(lst), sum(y for x, y in lst) // len(lst)) if lst else (0, 0)

print("Purple center:", avg(purple), f"({len(purple)} points)")
print("Pink center:", avg(pink), f"({len(pink)} points)")
print("Orange center:", avg(orange), f"({len(orange)} points)")

