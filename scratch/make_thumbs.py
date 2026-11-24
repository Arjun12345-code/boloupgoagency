from PIL import Image

for name in ['boloupgo.png', 'boloupgoagency.png', 'bolohero.png', 'bolo.png']:
    im = Image.open('assets/images/' + name)
    thumb = im.copy()
    thumb.thumbnail((200, 200))
    thumb.save(f'scratch/{name}_thumb.png', 'PNG')
    print(f'Saved scratch/{name}_thumb.png, original size: {im.size}')
