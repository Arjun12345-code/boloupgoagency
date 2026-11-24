import requests, time, re

r_live = requests.get('https://boloupgoagency.com/?nocache=' + str(time.time()), headers={'User-Agent': 'Mozilla/5.0'})
print('Live page length:', len(r_live.text))
print('Has 2527626 on live page:', '2527626' in r_live.text)
print('Has agency-id-callout on live page:', 'agency-id-callout' in r_live.text)
print('Has Step 4 on live page:', 'Step 4' in r_live.text)
print('Stylesheet links:', re.findall(r'href=[\'"][^\'"]*style\.css[^\'"]*[\'"]', r_live.text))
