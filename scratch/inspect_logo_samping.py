from PIL import Image

im = Image.open('assets/images/logo-samping.png')
print("logo-samping.png size:", im.size)
# Let's save a thumb to inspect or print non-empty regions
im.thumbnail((300, 100))
print("Thumbnail size:", im.size)

