from PIL import Image

im = Image.open('assets/images/boloup-header-logo.png')
print("Width:", im.width, "Height:", im.height)
# Let's inspect where text is
alpha = im.split()[-1]
print("Alpha bbox:", alpha.getbbox())

