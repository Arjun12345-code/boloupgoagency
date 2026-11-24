from PIL import Image

im = Image.open('assets/images/cropped-boloup.png').convert('RGB')
print("Dimensions:", im.size)

# Sample along the shape of the logo
# Let's find all distinct hues/regions
colors = []
for y in range(0, im.height, 10):
    for x in range(0, im.width, 10):
        r, g, b = im.getpixel((x, y))
        if r > 40 or g > 40 or b > 40:
            if not (r < 30 and g < 30 and b < 30):
                colors.append((x, y, r, g, b))

print("Total sampled emblem points:", len(colors))
# Find min/max colors
# Sort by red vs blue
pink_points = [p for p in colors if p[2] > 200 and p[4] > 100]
purple_points = [p for p in colors if p[4] > 150 and p[2] < 180]
orange_points = [p for p in colors if p[2] > 180 and p[3] > 80 and p[4] < 60]

print(f"Pink points: {len(pink_points)}, sample: {[f'#{p[2]:02x}{p[3]:02x}{p[4]:02x}' for p in pink_points[:3]]}")
print(f"Purple points: {len(purple_points)}, sample: {[f'#{p[2]:02x}{p[3]:02x}{p[4]:02x}' for p in purple_points[:3]]}")
print(f"Orange/Amber points: {len(orange_points)}, sample: {[f'#{p[2]:02x}{p[3]:02x}{p[4]:02x}' for p in orange_points[:3]]}")

