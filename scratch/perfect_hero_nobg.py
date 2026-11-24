from PIL import Image
import numpy as np

img = Image.open('scratch/boloupgoagency_clean_nobg.png').convert('RGBA')
arr = np.array(img, dtype=np.float32)

h, w = arr.shape[:2]
fade_height = 45 # bottom 45 pixels fade to 0

# Apply smooth linear fade to alpha on bottom fade_height rows
for i in range(fade_height):
    row_idx = h - fade_height + i
    factor = (fade_height - i - 1) / float(fade_height)
    arr[row_idx, :, 3] = arr[row_idx, :, 3] * factor

# Convert back to uint8
arr = np.clip(arr, 0, 255).astype(np.uint8)
perfect_img = Image.fromarray(arr, 'RGBA')

# Verify bottom row alpha is now 0
bottom_alpha = arr[-1, :, 3]
print("Bottom row alpha max:", bottom_alpha.max(), "mean:", bottom_alpha.mean())

# Save to assets/images/boloupgoagency-nobg.png and webp
perfect_img.save('assets/images/boloupgoagency-nobg.png', 'PNG', optimize=True)
perfect_img.save('assets/images/boloupgoagency-nobg.webp', 'WEBP', quality=95)
print("Saved assets/images/boloupgoagency-nobg.png & .webp successfully!")

