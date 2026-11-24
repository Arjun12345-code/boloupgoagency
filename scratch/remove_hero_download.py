def remove_hero_download(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target = '''              <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-lg" id="hero-btn-download">
                Download BoloUp Go
              </a>\n'''
    if target in content:
        content = content.replace(target, '')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed extra hero button from {filepath}!")
    else:
        print(f"Target not found in {filepath}!")

remove_hero_download('index.html')
remove_hero_download('preview.html')

