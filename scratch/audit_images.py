import re

for fn in ['header.html', 'footer.html', 'index.html', 'preview.html']:
    content = open(fn, encoding='utf-8').read()
    print(f'=== {fn} ===')
    for m in re.finditer(r'<img\s+([^>]+)>', content):
        attrs = m.group(1)
        src = re.search(r'src=[\"\']([^\"\']+)[\"\']', attrs)
        alt = re.search(r'alt=[\"\']([^\"\']*)[\"\']', attrs)
        width = re.search(r'width=[\"\']([^\"\']+)[\"\']', attrs)
        height = re.search(r'height=[\"\']([^\"\']+)[\"\']', attrs)
        loading = re.search(r'loading=[\"\']([^\"\']+)[\"\']', attrs)
        fetchpriority = re.search(r'fetchpriority=[\"\']([^\"\']+)[\"\']', attrs)

        src_val = src.group(1) if src else "NONE"
        alt_val = alt.group(1) if alt else "NONE"
        w_val = width.group(1) if width else "NONE"
        h_val = height.group(1) if height else "NONE"
        load_val = loading.group(1) if loading else (fetchpriority.group(1) if fetchpriority else "DEFAULT")

        # In lightbox modal, img is a dynamic placeholder
        if 'lightbox-img' in attrs:
            print(f'  [LIGHTBOX DYNAMIC IMG] src={src_val}')
            continue

        valid = bool(alt_val and alt_val != "NONE" and w_val != "NONE" and h_val != "NONE")
        print(f'  [IMG {"OK" if valid else "WARN"}] src={src_val}')
        print(f'        alt="{alt_val}" | width={w_val} | height={h_val} | loading={load_val}')

