import rembg
from PIL import Image
import numpy as np

print("Running rembg on assets/images/boloupgoagency.png...")
input_img = Image.open('assets/images/boloupgoagency.png')
output_img = rembg.remove(input_img)

# Save result
output_img.save('scratch/boloupgoagency_clean_nobg.png', 'PNG')

# Analyze alpha channel
arr = np.array(output_img)
alpha = arr[:, :, 3]
print("Clean alpha - zero:", np.sum(alpha == 0), "opaque:", np.sum(alpha == 255), "semi:", np.sum((alpha > 0) & (alpha < 255)))
print("Clean bottom row alpha mean:", alpha[-1, :].mean(), "max:", alpha[-1, :].max())
print("Saved scratch/boloupgoagency_clean_nobg.png successfully!")

