from PIL import Image

im = Image.open('assets/images/logo-samping.png').convert('L')
im = im.resize((100, 20))
for y in range(20):
    line = "".join(["#" if im.getpixel((x, y)) > 100 else " " for x in range(100)])
    print(line)

