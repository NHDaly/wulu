
import feedfinder as feed
import urllib2 as url
import xml.etree.ElementTree as ET

'''
return the xml string for the input url
'''
appName = 'WuLu'

def getXmlFromUrl(url_addr):
    page = url.urlopen(feed.feed(url_addr))
    string = ''
    for line in page:
    	string += line

    return string

def createPodcastXml(url_addr):
    xmlString=getXmlFromUrl(url_addr)
    tree = ET.fromstring(xmlString)
    #get items out of tree, add to database w/ entry from
    #item title to item link
    with open('itemsDb','wa') as itemsFile: 
        #deleting all items in podcastXML
        for chan in tree:
            for item in chan.findall('item'):
                itemsFile.write(ET.tostring(item)+'\n')
                chan.remove(item)
            #append to title    
            chan.find('title').text+= ' '+ appName + ' Audio Podcast'
    return ET.tostring(tree)