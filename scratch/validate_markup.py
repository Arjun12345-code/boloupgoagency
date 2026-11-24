import re

def check_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"=== Checking {filename} ===")
    print("Length:", len(content))
    # Check for unclosed tags or syntax issues
    for tag in ['header', 'nav', 'main', 'footer', 'section', 'article']:
        opens = len(re.findall(rf'<{tag}\b', content))
        closes = len(re.findall(rf'</{tag}>', content))
        if opens != closes:
            print(f"MISMATCH in {tag}: {opens} open vs {closes} close")
        else:
            print(f"Tag {tag}: {opens} pairs OK")

check_file('index.html')
check_file('preview.html')
check_file('header.html')
check_file('footer.html')

