from PIL import Image

im = Image.open('assets/images/boloup-app-icon.png').convert('RGB')
print("App icon size:", im.size)
# Sample diagonal from top-left to bottom-right
print("Diagonal samples from top-left (0,0) to bottom-right (260, 260):")
for i in range(10, 250, 25):
    r, g, b = im.getpixel((i, i))
    print(f"  ({i}, {i}): #{r:02x}{g:02x}{b:02x} RGB({r}, {g}, {b})")

