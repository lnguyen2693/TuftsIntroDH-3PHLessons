# obo.py
def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).

def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

def wordListToFreqDict(wordlist):
    d = {}
    for w in wordlist:
        if w not in d:
            d[w] = 0
        d[w] += 1
    
    return list(map(lambda x: (d[x], x), d))

def sortFreqDict(dictionary):
    return sorted(dictionary, reverse=True)
