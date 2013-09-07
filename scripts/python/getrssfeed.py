
import feedfinder as feedfind
import urllib2 as url
import xml.etree.ElementTree as ET

'''
return the xml string for the input url
'''
appName = 'WuLu'

def getXmlFromUrl(url_addr):
    # TODO make sure to ask user for which feed
    # (call feedfind.feeds() not feed)
    page = url.urlopen(feedfind.feed(url_addr))
    string = ''
    for line in page:
    	string += line

    return string

def createPodcastXml(url_addr):
    xmlString=getXmlFromUrl(url_addr)
    tree = ET.fromstring(xmlString)
    #get items out of tree, add to database w/ entry from
    #item title to item link
    with open('itemsDb','a') as itemsFile: 
        #deleting all items in podcastXML
        for chan in tree:
            for item in chan.findall('item'):
                itemsFile.write(ET.tostring(item)+'\n')
                chan.remove(item)
            #append to title    
            chan.find('title').text+= ' '+ appName + ' Audio Podcast'
    return ET.tostring(tree)


from sys import argv

if __name__ == "__main__":
    try:
    	print createPodcastXml(argv[1])
    except Exception, e:
        print "ERRORRRRR!", e

