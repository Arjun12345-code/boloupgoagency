with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('class="hero-img-wrap"')
end = c.find('</div>', start+50)
print(c[start:end+10])

