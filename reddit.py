import urllib
import json
from collections import defaultdict

serviceurl = 'https://www.reddit.com/r/'

while True:
    subreddit = raw_input('Enter subreddit: ')
    if len(subreddit) < 1 : subreddit = 'music';
    if subreddit == 'end': break

    url = serviceurl + subreddit + '.json'
    print 'Retrieving /r/' + subreddit.capitalize()
    uh = urllib.urlopen(url)
    data = uh.read()

    try: js = json.loads(str(data))
    except: js = None

    # print json.dumps(js, indent=4)
    contents = js['data']['children']
    for items in contents:
        if items['data']['domain'] == 'youtube.com' :
            youtubeUrl = items['data']['url']
            videoTitle = items['data']['title']

            print videoTitle, youtubeUrl