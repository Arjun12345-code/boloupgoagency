from PIL import Image
import numpy as np

img = Image.open('scratch/boloupgoagency_clean_nobg.png')
arr = np.array(img)
alpha = arr[:, :, 3]

bins = [0, 1, 50, 100, 150, 200, 254, 255]
counts, _ = np.histogram(alpha, bins=bins)
for i in range(len(counts)):
    print(f"Alpha {bins[i]}..{bins[i+1]}: {counts[i]}")

