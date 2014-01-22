import urllib2 as url
import xml.etree.ElementTree as ET
import json
from sys import argv
import logging

appName = 'WuLu'

# ======= HELPER FUNCTIONS =========

def getPodcastXmlFromUrl(url_addr):
    ''' given an rss feed url, parse and create a pocast rss xml. '''
    
    page = url.urlopen(url_addr)
    string = ''
    for line in page:
    	string += line
    
    return string

def getChildren(elt, tag):
    return [x for x in elt if x.tag[-len(tag):] == tag] 

def getChild(elt, tag):
    tag_list = getChildren(elt, tag)
    if not len(tag_list) > 0:
       raise Exception, 'Tag: ' + tag + ' not found in elt: ' + str(elt)
    return tag_list[0]


def recursiveFindChildren(elt, tag):
    children = []
    recursiveFindChildren_helper(elt, tag, children)
    return children

def recursiveFindChildren_helper(elt, tag, children):
    children += getChildren(elt, tag)
    for child in elt:
        recursiveFindChildren_helper(child, tag, children)

        

# ====== XML Searching helpers =======

def findPossibleTag(elt, possible_tags):
    text = ''
    found = False

    for tag in possible_tags:
        if found:
        	break
        try:
            text = getChild(elt, tag).text
            found = True
        except:
            pass

    return text

def findAuthor(elt):
    return findPossibleTag(elt, ['author', 'publisher'])

def findDescription(elt):
    return findPossibleTag(elt, ['description', 'summary'])

def findSubtitle(elt):
    return findPossibleTag(elt, ['subtitle'])

def findLink(elt):
    return findPossibleTag(elt, ['link'])

def findCategory(elt):
    return findPossibleTag(elt, ['category'])

def findCopyright(elt):
    return findPossibleTag(elt, ['copyright'])

def findPubDate(elt):
    return findPossibleTag(elt, ['pubDate'])


# ======= MAIN FUNCTIONS =========

xml_top_str_c = '''<?xml version="1.0" encoding="UTF-8"?>'''

class PodcastXMLData(object):
    def __init__(self):
        self.title = ''
        self.author = ''
        self.description = ''
        self.subtitile = ''
        self.link = ''
        self.category = ''
        self.copyright = ''
        self.iconArtLink = ''
        self.children = [] # an array of ItemXMLData structs
        
class ItemXMLData(object):
    def __init__(self):
        self.title = ''
        self.subtitle = ''
        self.description = '' # summary?
        self.author = ''
        self.pubDate = ''
        self.guid = ''
        self.duration = ''

def loadPodcastXMLData(tree):

    xmlData = PodcastXMLData()
    
    # Find channel. ... really should be the first element, though.
    rss = tree
    while 'channel' not in rss[0].tag:
    	rss = rss[0]
    	
    chan = rss[0] # really should only be one chan...

    title = getChild(chan, 'title')
    xmlData.title = title.text + ' ' + appName + ' Audio Podcast'
    xmlData.author = findAuthor(chan)
    xmlData.description = findDescription(chan)
    xmlData.subtitle = findSubtitle(chan)
    xmlData.link = findLink(chan)
    xmlData.category = findCategory(chan)
    xmlData.copyright = findCopyright(chan)
    
    for item in recursiveFindChildren(tree, 'item'):
        xmlItem = ItemXMLData()
        xmlItem.title = getChild(item, 'title').text
        xmlItem.link = findLink(item)
        xmlItem.pubDate = findPubDate(item)
        if xmlItem.pubDate == '':
            xmlItem.pubDate = 'BAD_DATE' 

        xmlData.children.append(xmlItem)

    return xmlData

def createNewPodcastFromXMLData(xmlData):
    
    # set up rss
    tree = ET.Element('rss')
    tree.set('xmlns:itunes', 'http://www.itunes.com/dtds/podcast-1.0.dtd')
    tree.set('version', '2.0') 

    # set up podcast:
    chan = ET.SubElement(tree, 'channel')

    title = ET.SubElement(chan, 'title')
    title.text = xmlData.title

    link = ET.SubElement(chan, 'link')
    link.text = xmlData.link

    copyright = ET.SubElement(chan, 'copyright')
    copyright.text = xmlData.copyright

    subtitle = ET.SubElement(chan, 'itunes:subtitle')
    subtitle.text = xmlData.subtitle

    author = ET.SubElement(chan, 'itunes:author')
    author.text = xmlData.author

    summary = ET.SubElement(chan, 'itunes:summary')
    summary.text = xmlData.description

    description = ET.SubElement(chan, 'description')
    description.text = xmlData.description
    
    if (xmlData.iconArtLink):
        image  = ET.SubElement(chan, 'itunes:image')
        image.set('href', xmlData.iconArtLink)

    if (xmlData.iconArtLink):
        category = ET.SubElement(chan, 'itunes:category')
        category.text = xmlData.category


    # CHILDREN ARE ENTERED IN A DIFFERENT SCRIPT!
    '''
    for child in xmlData.children:
        
        item = ET.SubElement(chan, 'item')

        title = ET.SubElement(item, 'title')
        title.text = child.title

        author = ET.SubElement(item, 'itunes:author')
        author.text = child.author

        summary = ET.SubElement(item, 'itunes:summary')
        summary.text = child.description

        subtitle = ET.SubElement(item, 'subtitle')
        subtitle.text = child.subtitle

        description = ET.SubElement(item, 'description')
        description.text = child.description

        guid = ET.SubElement(item, 'guid')
        guid.text = child.guid

        enclosure = ET.SubElement(item, 'enclosure')
        enclosure.set('url', '')
        enclosure.set('length', '')
        enclosure.set('type', 'audio/x-m4a')

        pubDate = ET.SubElement(item, 'pubDate')
        pubDate.text = child.pubDate

        duration = ET.SubElement(item, 'itunes:duration')
        duration.text = child.duration
    '''

    xml_out = ''    
    xml_out += xml_top_str_c + '\n'

    dump = ET.tostring(tree)
    xml_out += dump

    return xml_out

def createPodcastXml(url_addr):
    xmlString=getPodcastXmlFromUrl(url_addr)
    tree = ET.fromstring(xmlString)
    
    xmlData = loadPodcastXMLData(tree)

    xml_out = createNewPodcastFromXMLData(xmlData)
    
    articleList = [x.__dict__ for x in xmlData.children]
    return json.dumps({'XML':xml_out, 'episodes':articleList})


# set up logging errors
logging.basicConfig(level=logging.DEBUG, filename='/home/vagrant/wulu_errors.log')

if __name__ == '__main__':
    try:
      print createPodcastXml(argv[1])
    except:
        logging.exception('In file, '+ argv[0] +', exception:')

