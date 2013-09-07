
from goose import Goose
from sys import argv 
import json

g = Goose()

# NOTE, on error this will return ''. Caller should check for this
# and not try to text-to-speech it.
cleanText=g.extract(argv[1]).cleaned_text
cleanText=cleanText.strip(' \t\n\r')
print json.dumps(cleanText)

