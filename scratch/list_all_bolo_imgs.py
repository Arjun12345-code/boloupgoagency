import os
from PIL import Image

for f in sorted(os.listdir('assets/images')):
    if 'bolo' in f.lower() or 'logo' in f.lower() or 'icon' in f.lower():
        p = os.path.join('assets/images', f)
        if os.path.isfile(p):
            try:
                im = Image.open(p)
                print(f"{f:35} size={str(im.size):15} mode={im.mode}")
            except Exception as e:
                print(f"{f:35} error: {e}")

