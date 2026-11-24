from PIL import Image

for name in ['boloupgoagency.png', 'boloupgo.png', 'bolohero.png', 'bolo.png']:
    im = Image.open('assets/images/' + name)
    print(f"{name:25} size={str(im.size):15} mode={im.mode}")

