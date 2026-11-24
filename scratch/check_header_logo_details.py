from PIL import Image

im = Image.open('assets/images/boloup-header-logo.png')
print("Size:", im.size)
# Let's inspect non-transparent pixels
alpha = im.split()[-1]
bbox = alpha.getbbox()
print("Non-transparent bbox:", bbox)

