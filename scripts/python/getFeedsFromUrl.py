
import feedfinder as feedfind
import json
from sys import argv

def getFeedsFromUrl(url_addr):
    ''' Checks url_addr for any rss feeds and returns their '''\
    '''urls as a json array. '''

    feeds = feedfind.feeds(url_addr)
    return json.dumps(feeds)

if __name__ == "__main__":
    try:
    	print getFeedsFromUrl(argv[1])
    except :
        print "ERRORRRRR!"

