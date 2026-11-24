from PIL import Image

im = Image.open('assets/images/boloup-app-icon.png')
print("app-icon size:", im.size, "mode:", im.mode)
bbox = im.getbbox()
print("app-icon bbox:", bbox)

