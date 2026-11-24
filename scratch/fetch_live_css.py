import requests

r = requests.get('https://boloupgoagency.com/wp-content/themes/hello-elementor-child/style.css?ver=2.5.0')
print("Status:", r.status_code, "Length:", len(r.text))
start = r.text.find('body {')
print(r.text[start:start+500])

