from PIL import Image

im = Image.open('assets/images/boloup-header-logo.png').convert('L')
im = im.resize((60, 20))
for y in range(20):
    line = "".join(["#" if im.getpixel((x, y)) > 100 else " " for x in range(60)])
    print(line)

