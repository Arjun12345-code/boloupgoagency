from PIL import Image

def inspect_nobg(path):
    im = Image.open(path)
    print(f"\n=== Inspecting {path} ===")
    print("Size:", im.size, "Mode:", im.mode)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # Check corner pixels
    corners = [(0, 0), (im.width-1, 0), (0, im.height-1), (im.width-1, im.height-1)]
    print("Corner pixels (RGBA):", [im.getpixel(c) for c in corners])
    # Check alpha values distribution
    alphas = [a for _, _, _, a in im.getdata()]
    transparent = sum(1 for a in alphas if a == 0)
    semitrans = sum(1 for a in alphas if 0 < a < 255)
    opaque = sum(1 for a in alphas if a == 255)
    print(f"Total: {len(alphas)} | Transparent (0): {transparent} ({transparent*100/len(alphas):.1f}%) | Semi: {semitrans} | Opaque (255): {opaque}")

for f in ['assets/images/boloupgoagency-nobg.png', 'assets/images/boloupgo-nobg.png', 'assets/images/boloup-hero-cutout.png', 'assets/images/bolohero-nobg.png']:
    inspect_nobg(f)

