from PIL import Image

def sample_gradient(path):
    im = Image.open(path).convert('RGBA')
    print(f"\nSampling {path} across width at center height:")
    y = im.height // 2
    samples = []
    for x in range(0, im.width, max(1, im.width // 15)):
        r, g, b, a = im.getpixel((x, y))
        if a > 100:
            samples.append((x, f"#{r:02x}{g:02x}{b:02x}", (r, g, b)))
    for s in samples:
        print(f"  x={s[0]}: {s[1]} {s[2]}")

sample_gradient('assets/images/logo-samping.png')
sample_gradient('assets/images/boloup-logo-highres.png')
sample_gradient('assets/images/boloup-horizontal-logo.png')

