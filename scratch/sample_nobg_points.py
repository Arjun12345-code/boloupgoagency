from PIL import Image

im = Image.open('assets/images/boloupgoagency-nobg.png')
print("boloupgoagency-nobg.png size:", im.size)

# Let's inspect non-transparent pixels outside the central character
# Let's sample a few points that should be empty background
samples = [
    (50, 50), (100, 100), (200, 100), (800, 100), (900, 100),
    (50, 500), (100, 500), (900, 500), (950, 500),
    (50, 1000), (100, 1000), (900, 1000), (950, 1000)
]
for x, y in samples:
    p = im.getpixel((x, y))
    print(f"Point ({x}, {y}): RGBA = {p}")

