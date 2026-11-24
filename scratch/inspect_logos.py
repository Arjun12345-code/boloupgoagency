import os
from PIL import Image

for name in ['boloup-header-logo.png', 'boloup-horizontal-logo.png', 'logo-samping.png', 'boloup-app-icon.png', 'cropped-boloup.png']:
    p = os.path.join('assets/images', name)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{name}: size={im.size}, mode={im.mode}")

