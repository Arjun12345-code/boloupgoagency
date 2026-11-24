from PIL import Image

for name in ['boloup-hero-cutout.png', 'bolohero-nobg.png', 'boloupgo-nobg.png', 'boloupgoagency-nobg.png', 'bolo-nobg.png']:
    im = Image.open('assets/images/' + name)
    print(f"{name:30} size={str(im.size):15} mode={im.mode}")
    im.thumbnail((200, 200))
    im.save(f"scratch/{name.replace('.png', '_thumb.png')}")
print("Saved all cutout thumbs")

