import requests

r_meta = requests.get('https://boloupgoagency.com/?dump_meta=1')
data = r_meta.json()
widget_html = data[0]['elements'][0]['settings']['html']
print("Length of widget_html:", len(widget_html))
idx = widget_html.find('<picture>')
print(widget_html[idx:idx+350])

