import re

def remove_badge(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = re.sub(r'\s*<span class="brand-badge">Agency</span>', '', c)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Removed brand-badge from {filepath}!")

remove_badge('header.html')
remove_badge('footer.html')
remove_badge('preview.html')

