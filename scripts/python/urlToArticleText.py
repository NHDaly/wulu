
from goose import Goose
from sys import argv 
import json

g = Goose()

# NOTE, on error this will return ''. Caller should check for this
# and not try to text-to-speech it.
print json.dumps(g.extract(argv[1]).cleaned_text)

