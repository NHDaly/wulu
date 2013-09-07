
import feedfinder as feed
import urllib2 as url

'''
return the xml string for the input url
'''

def getXmlFromURL(url_addr):
    page = url.urlopen(feed.feed(url_addr))
    string = ''
    for line in page:
    	string += line

    return string

