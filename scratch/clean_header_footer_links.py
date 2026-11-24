with open('header.html', 'r', encoding='utf-8') as f:
    h = f.read()
h = h.replace('<link rel="stylesheet" href="style.css">\n\n', '')
with open('header.html', 'w', encoding='utf-8') as f:
    f.write(h)

with open('footer.html', 'r', encoding='utf-8') as f:
    ft = f.read()
ft = ft.replace('<link rel="stylesheet" href="style.css">\n\n', '')
with open('footer.html', 'w', encoding='utf-8') as f:
    f.write(ft)

print("Removed relative style.css links from header.html and footer.html!")

