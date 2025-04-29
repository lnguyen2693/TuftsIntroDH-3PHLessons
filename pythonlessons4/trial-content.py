# trial-content.py

import urllib.request, urllib.error, urllib.parse, obo

url = 'https://www.oldbaileyonline.org/about/empire-and-the-old-bailey'

response = urllib.request.urlopen(url)
HTML = response.read().decode('UTF-8')

print(obo.stripTags(HTML))