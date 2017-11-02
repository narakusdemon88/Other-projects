import requests
import json

r = requests.get('https://www.reddit.com/r/worldnews.json', headers = {'User-agent': 'Chrome'})

theJSON = json.loads(r.text)

for items in theJSON:
	print items