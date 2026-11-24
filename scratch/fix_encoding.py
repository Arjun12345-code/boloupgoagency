for fn in ['index.html', 'preview.html', 'wp_template.php']:
    with open(fn, 'rb') as f:
        data = f.read()
    
    # Replace any single byte 0x96 with utf-8 0xe2 0x80 0x93 (en-dash '–')
    fixed = data.replace(b'\x96', '–'.encode('utf-8'))
    
    with open(fn, 'wb') as f:
        f.write(fixed)
    print(f'Fixed {fn}')

