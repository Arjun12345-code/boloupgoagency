with open(r'c:\Users\asus\Desktop\WordPress\boloupgoagent\no-hero.html', 'r', encoding='utf-8') as f:
    c = f.read()
print("Length of no-hero.html:", len(c))
# check hero section
start = c.find('id="hero"')
if start != -1:
    print(c[start-30:start+300])
else:
    print("No id='hero' found in no-hero.html!")

