from PIL import Image
import numpy as np

img = Image.open('assets/images/boloupgoagency-nobg.png')
print('Size:', img.size, 'Mode:', img.mode)

arr = np.array(img)
alpha = arr[:, :, 3]
print('Alpha min:', alpha.min(), 'max:', alpha.max())
print('Total pixels:', alpha.size)
print('Zero alpha (fully transparent):', np.sum(alpha == 0))
print('Full alpha (opaque):', np.sum(alpha == 255))
print('Semi-transparent:', np.sum((alpha > 0) & (alpha < 255)))

# Check the corners (0,0), (1023,0), (0,1535), (1023,1535)
print('Top-left alpha:', alpha[0, 0])
print('Top-right alpha:', alpha[0, -1])
print('Bottom-left alpha:', alpha[-1, 0])
print('Bottom-right alpha:', alpha[-1, -1])

# Check bottom row
print('Bottom row alphas min/max/mean:', alpha[-1, :].min(), alpha[-1, :].max(), alpha[-1, :].mean())
# How many non-zero pixels in bottom row:
print('Non-zero in bottom row:', np.sum(alpha[-1, :] > 0))

