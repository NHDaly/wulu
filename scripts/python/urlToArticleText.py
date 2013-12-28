
from goose import Goose
from sys import argv 
from updatePodcastWithDatabase import site_dir
import json

g = Goose()

# NOTE, on error this will return ''. Caller should check for this
# and not try to text-to-speech it.
url = argv[1] 
cleanText=g.extract(url).cleaned_text
cleanText=cleanText.strip(' \t\n\r')

# Some websites need cookies to read them (eg NYTimes).
# If reading fails, try again with cookies
if (cleanText == ''):
    print "EMPTY CLEAN TEXT"
    import urllib2
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(url)
    
    raw_html = response.read()
    a = g.extract(raw_html=raw_html)
    cleanText = a.cleaned_text


with open(site_dir+'/podcasts/textout.txt', 'w') as argsoutFile:
    argsoutFile.write(cleanText.encode('utf8'))
print json.dumps(cleanText)

