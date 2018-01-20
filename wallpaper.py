import urllib
import urllib2
import json 
from collections import defaultdict

serviceurl = 'https://www.reddit.com'

while True:
    subreddit = raw_input('What kind of wallpapers?: ')
    # currently not working
    # just hit enter for now
    if len(subreddit) < 1 : subreddit = 'wallpapers';
    if subreddit == 'anime':
        url = 'https://www.reddit.com/r/Animewallpaper/top/.json?sort=top'
    if subreddit == 'end': break

    if subreddit != 'mine': 
        url = serviceurl + '/r/' + subreddit + '/top/.json?sort=top'
        print 'Retrieving /r/' + subreddit.capitalize() + ' from ' + url
    uh = urllib.urlopen(url)
    data = uh.read()

    try: js = json.loads(str(data))
    except: js = None

    contents = js['data']['children']
    for items in contents:
        if items['data']['domain'] == 'i.imgur.com' :
            imgurUrl = items['data']['url']
            imgurTitle = items['data']['title']
            imgurFileType = imgurUrl[-4:]

            def downloadWebImage(url):
                request = urllib2.Request(url)
                img = urllib2.urlopen(request).read()
                with open (imgurTitle + imgurFileType, 'w') as f: f.write(img)

            downloadWebImage(imgurUrl)

            print imgurTitle, imgurUrl, imgurFileType