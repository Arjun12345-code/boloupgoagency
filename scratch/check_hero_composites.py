from PIL import Image

im = Image.open('assets/images/boloupgoagency-nobg.png')

# Create a composite on dark background and on pure white to see any artifacts
bg_dark = Image.new('RGBA', im.size, (6, 9, 14, 255))
bg_dark.paste(im, (0, 0), im)
bg_dark.thumbnail((600, 900))
bg_dark.save('scratch/hero_on_dark.png')

# Also check boloupgo-nobg.png and bolohero-nobg.png
im2 = Image.open('assets/images/boloupgo-nobg.png')
bg_dark2 = Image.new('RGBA', im2.size, (6, 9, 14, 255))
bg_dark2.paste(im2, (0, 0), im2)
bg_dark2.thumbnail((600, 600))
bg_dark2.save('scratch/hero_on_dark2.png')

print("Composites saved!")

