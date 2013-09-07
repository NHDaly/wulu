import urllib2 as url
import xml.etree.ElementTree as ET
import json
from sys import argv

appName = 'WuLu'

def getPodcastXmlFromUrl(url_addr):
    ''' given an rss feed url, parse and create a pocast rss xml. '''
    
    page = url.urlopen(url_addr)
    string = ''
    for line in page:
    	string += line
    
    return string

def createPodcastXml(url_addr):
    xmlString=getPodcastXmlFromUrl(url_addr)
    tree = ET.fromstring(xmlString)
    #get items out of tree, add to database w/ entry from
    #item title to item link
    articleList=[]
    #deleting all items in podcastXML
    for chan in tree:
        chan.find('title').text+= ' '+ appName + ' Audio Podcast'
        for item in chan.findall('item'):
           # itemsFile.write(ET.tostring(item)+'\n')
           articleTitle = item.find('title').text
           articleUrl = item.find('link').text
           articlePubDate = item.find('pubDate').text
           articleList.append({'rss_url':rssUrl,'title':articleTitle,'site_url':articleUrl,'pub_date':articlePubDate}) 
           chan.remove(item)
           #append to title    
    return json.dumps({'XML':ET.tostring(tree),'episodes':articleList})


if __name__ == "__main__": 
    try:
      print createPodcastXml(argv[1])
      #print argv[1]
    except :
      print "ERRORRRRR!"

