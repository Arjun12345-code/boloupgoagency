from PIL import Image

def analyze_img(path):
    im = Image.open(path)
    print(f"=== {path} ===")
    print("Size:", im.size, "Mode:", im.mode)

for p in ['assets/images/boloup-header-logo.png', 'assets/images/boloup-horizontal-logo.png', 'assets/images/logo-samping.png', 'assets/images/boloup-transparent-logo.png']:
    analyze_img(p)

