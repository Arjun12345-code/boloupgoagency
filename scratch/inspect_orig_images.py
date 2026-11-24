from PIL import Image

for name in ['boloupgo.png', 'boloupgoagency.png', 'bolohero.png', 'bolo.png']:
    try:
        im = Image.open('assets/images/' + name)
        print(name, im.size, im.mode)
    except Exception as e:
        print(name, 'error:', e)

