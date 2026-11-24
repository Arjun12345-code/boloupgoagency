from PIL import Image

im = Image.open('assets/images/boloupgoagency.png')
print("Original boloupgoagency.png size:", im.size)
im.thumbnail((400, 600))
im.save('scratch/boloupgoagency_thumb.png')

# Also inspect boloupgo.png
im2 = Image.open('assets/images/boloupgo.png')
print("Original boloupgo.png size:", im2.size)
im2.thumbnail((400, 400))
im2.save('scratch/boloupgo_thumb.png')

print("Thumbnails saved!")

