import re

for fn in ['header.html', 'footer.html', 'index.html', 'preview.html']:
    content = open(fn, encoding='utf-8').read()
    print(f'=== {fn} ===')
    for m in re.finditer(r'<a\s+([^>]+)>', content):
        attrs = m.group(1)
        href_m = re.search(r'href=[\"\']([^\"\']+)[\"\']', attrs)
        if not href_m:
            continue
        href = href_m.group(1)
        is_external = href.startswith('http://') or href.startswith('https://')
        has_blank = 'target="_blank"' in attrs
        has_rel = 'rel="noopener noreferrer"' in attrs
        if is_external:
            if not (has_blank and has_rel):
                print(f'  [EXTERNAL MISMATCH] {href} -> blank:{has_blank}, rel:{has_rel}')
            else:
                print(f'  [EXTERNAL OK] {href}')
        else:
            print(f'  [INTERNAL OK] {href}')

