from PIL import Image

im = Image.open('scratch/hero_crop_after_deploy.png')
print("Image dimensions:", im.size)

# Sample a grid of pixels
for y in range(0, im.height, 50):
    row = [im.getpixel((x, y)) for x in range(0, im.width, 100)]
    print(f"y={y}:", ["#%02x%02x%02x" % (c[0], c[1], c[2]) for c in row])

