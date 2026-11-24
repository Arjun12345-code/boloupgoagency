from PIL import Image

for name in ['boloupgo.png', 'boloupgoagency.png', 'bolohero.png', 'bolo.png', 'boloupgoagency-nobg.png']:
    im = Image.open('assets/images/' + name)
    print(f"=== {name} ===")
    print(f"Format: {im.format}, Size: {im.size}, Mode: {im.mode}")
    # Sample center pixel, corners
    w, h = im.size
    print(f"Top-left: {im.getpixel((10, 10))}")
    print(f"Top-right: {im.getpixel((w-10, 10))}")
    print(f"Center: {im.getpixel((w//2, h//2))}")
    print(f"Bottom-center: {im.getpixel((w//2, h-10))}")
