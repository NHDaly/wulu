import xml.etree.ElementTree as ET
import json
from sys import argv

webUrl = 'http://ec2-54-226-137-31.compute-1.amazonaws.com/podcasts'

def updatePodcastXml(rss_url, title, audio_filename, pubDate):
    with open(podcast_local_url, 'r') as xmlFile:
     xmlString=''.join([line for line in xmlFile])

     tree = ET.fromstring(xmlString)
     
     chan = tree.find('channel')
     
     item = ET.SubElement(chan, 'item')
     
     #add subinfor for item
     it_title = ET.SubElement(item, 'title')
     it_title.text = title
     
     #TODO Find full audio web url
     audio_web_url = webUrl + rss_url + audio_filename


     #TODO Find length of audio file -- should we do this in php when adding to database?
     
     it_enclosure = ET.SubElement(item, 'enclosure', {'length':"12321",
                                                      'type':'audio/x-mp3'})
     it_enclosure.text = audio_web_url
     
     #TODO guid
     
     it_pubDate = ET.SubElement(item, 'pubDate')
     it_pubDate.text = pubDate

    return json.dumps({'XML':ET.tostring(tree),'episodes':articleList})



