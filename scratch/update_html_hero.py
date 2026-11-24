import re

for fname in ['index.html', 'preview.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the hero img tag
    old_pattern = r'<img\s+src=["\']assets/images/boloupgoagency\.png["\'][^>]*>'
    new_img = '''<picture>
                  <source srcset="assets/images/boloupgoagency-nobg.webp" type="image/webp">
                  <img src="assets/images/boloupgoagency-nobg.png"
                       alt="Build a Team That Grows with BoloUp Go Agency"
                       class="hero-img"
                       width="1024"
                       height="1536"
                       fetchpriority="high">
                </picture>'''
    
    if re.search(old_pattern, content):
        content = re.sub(old_pattern, new_img, content)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname} successfully")
    else:
        print(f"Pattern not found in {fname}")

