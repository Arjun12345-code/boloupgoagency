with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('id="benefits"')
end = c.find('</section>', start)
print(c[start-30:end+10])

