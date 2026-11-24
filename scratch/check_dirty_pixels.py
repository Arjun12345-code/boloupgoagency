from PIL import Image

im = Image.open('assets/images/boloupgoagency-nobg.png')

# Let's check how clean the cut is
# Check pixels with alpha between 1 and 200: are their RGB values dark/gray?
dirty_pixels = 0
for r, g, b, a in im.getdata():
    if 0 < a < 255:
        # Check if it's a dark residual edge
        if r < 40 and g < 40 and b < 40:
            dirty_pixels += 1

print("Total dirty dark semi-transparent edge pixels:", dirty_pixels)

