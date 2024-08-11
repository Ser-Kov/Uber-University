import requests


r = requests.get('https://api.github.com/events')
print(r.json())
print(r.status_code)
print(r.headers)
