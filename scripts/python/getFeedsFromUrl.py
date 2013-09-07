
import feedfinder as feedfind
import json

def getFeedsFromUrl(url_addr):
    ''' Checks url_addr for any rss feeds and returns their '''\
    '''urls as a json array. '''

    feeds = feedfind.feeds(url_addr)
    return json.dumps(feeds)


