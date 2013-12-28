
from goose import Goose
from sys import argv 
from updatePodcastWithDatabase import site_dir
import json

g = Goose()

# NOTE, on error this will return ''. Caller should check for this
# and not try to text-to-speech it.
cleanText=g.extract(argv[1]).cleaned_text
cleanText=cleanText.strip(' \t\n\r')
with open(site_dir+'/podcasts/textout.txt', 'w') as argsoutFile:
    argsoutFile.write(cleanText.encode('utf8'))
print json.dumps(cleanText)

