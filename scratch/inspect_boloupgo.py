from PIL import Image

for name in ['boloupgo.png', 'boloupgoagency.png', 'boloupgo-nobg.png', 'boloupgoagency-nobg.png']:
    im = Image.open('assets/images/' + name)
    print(name, im.size, im.mode)

