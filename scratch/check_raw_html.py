import requests

r = requests.get('https://boloupgoagency.com/?v=251')
idx = r.text.find('<picture>')
if idx != -1:
    print("Raw HTML picture tag:")
    print(r.text[idx:idx+350])
else:
    print("No <picture> found in raw HTML!")

