from PIL import Image

im = Image.open('scratch/hero_crop_after_deploy.png')
w, h = im.size
print("Crop dimensions:", w, h)
center_colors = [im.getpixel((x, y)) for x in range(w//4, 3*w//4, 20) for y in range(h//4, 3*h//4, 20)]
glow_pixels = [c for c in center_colors if c[0] > 100 and c[2] > 100]
print("Glow pixels count:", len(glow_pixels), "out of", len(center_colors))

# Check corner pixels of the hero image wrap area
# The background of the page is around #06090e -> (6, 9, 14)
print("Top-left pixel of hero crop:", im.getpixel((10, 10)))
print("Top-right pixel of hero crop:", im.getpixel((w-10, 10)))
print("Bottom-left pixel of hero crop:", im.getpixel((10, h-10)))
print("Bottom-right pixel of hero crop:", im.getpixel((w-10, h-10)))

