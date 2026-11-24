import requests, re, time

url = 'https://boloupgoagency.com/?v=' + str(time.time())
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
text = r.text

print('Stylesheet in live HTML:', re.findall(r'href=[\'"][^\'"]*style\.css[^\'"]*[\'"]', text))
print('Has 2527626:', '2527626' in text)
print('Has hero-badge:', 'hero-badge' in text)
print('Has section-badge:', 'section-badge' in text)
print('Has about-feature-tags:', 'about-feature-tags' in text)
print('Has earning-badge:', 'earning-badge' in text)
print('Has Step 4:', 'Step 4' in text)
print('Has final CTA text:', 'Your Next Great Team' in text)

