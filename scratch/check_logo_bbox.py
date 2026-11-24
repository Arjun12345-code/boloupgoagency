from PIL import Image

for name in ['boloup-header-logo.png', 'boloup-horizontal-logo.png', 'logo-samping.png']:
    im = Image.open('assets/images/' + name)
    print(name, im.size, im.getbbox())

