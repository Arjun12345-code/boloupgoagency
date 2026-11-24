from PIL import Image

im = Image.open('scratch/hero_crop_live.png')
# let's analyze colors around the hero image
# Is there a big pink/purple glowing circular blob?
w, h = im.size
print("Crop dimensions:", w, h)
# check center region
center_colors = [im.getpixel((x, y)) for x in range(w//4, 3*w//4, 20) for y in range(h//4, 3*h//4, 20)]
# count how many pixels are bright magenta / purple / glowing
glow_pixels = [c for c in center_colors if c[0] > 100 and c[2] > 100]
print("Glow pixels count:", len(glow_pixels), "out of", len(center_colors))
if glow_pixels:
    print("Sample glow colors:", glow_pixels[:5])

