from PIL import Image

im = Image.open('scratch/hero_final_verification.png')
print("Final crop dimensions:", im.size)

for y in range(0, im.height, 60):
    row = [im.getpixel((x, y)) for x in range(0, im.width, 100)]
    print(f"y={y:3d}:", ["#%02x%02x%02x" % (c[0], c[1], c[2]) for c in row])

