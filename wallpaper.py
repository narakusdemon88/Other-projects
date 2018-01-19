import urllib
import json 
from collections import defaultdict

serviceurl = 'https://www.reddit.com'

while True:
    subreddit = input('Enter subreddit: ')
    if len(subreddit) < 1 : subreddit = 'wallpapers';
    if subreddit == 'end': break

    if subreddit != 'mine': 
        url = serviceurl + '/r/' + subreddit + '/top/.json?sort=top'
        print ('Retrieving /r/' + subreddit.capitalize())
    uh = urllib.request.urlopen(url)
    data = uh.read()

    try: js = json.loads(str(data))
    except: js = None

    contents = js['data']['children']
    for items in contents:
        if items['data']['domain'] == 'i.imgur.com' :
            imgurUrl = items['data']['url']
            imgurTitle = items['data']['title']

            print (imgurTitle, imgurUrl)


import urllib.request

print('Beginning file download with urllib2...')

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
urllib.request.urlretrieve(url, '/Users/jon-erik.akashi/Desktop/test folder/cat.jpg')