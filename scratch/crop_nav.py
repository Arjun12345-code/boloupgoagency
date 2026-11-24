from PIL import Image

im = Image.open('.playwright-mcp/page-2026-11-07T07-56-37-985Z.png')
print("Screenshot size:", im.size)
# crop navbar
nav = im.crop((0, 0, im.width, 100))
nav.save('scratch/nav_preview.png')
print("Saved scratch/nav_preview.png")

