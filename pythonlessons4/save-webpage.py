# save-webpage.py

import urllib.request, urllib.error, urllib.parse

url = 'https://www.oldbaileyonline.org/about/empire-and-the-old-bailey'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

f = open('obo-t17800628-33.html', 'wb')
f.write(webContent)
f.close