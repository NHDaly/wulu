import xml.etree.ElementTree as ET
import json
from sys import argv
import logging
from constants import podcasts_folder_address, site_abs_directory

# set up logging errors
logging.basicConfig(level=logging.DEBUG, filename='/vagrant/wulu_errors.log')


webUrl = podcasts_folder_address
site_dir = site_abs_directory

def updatePodcastXml(rss_url, audio_filename, xmlItem):
   # load current xml file

   xmlFileUrl = site_dir+'podcasts/' + rss_url +'/podcast.xml'
   xmlString = ''
   with open(xmlFileUrl, 'r') as xmlFile:
       xmlString=''.join([line for line in xmlFile])

   tree = ET.fromstring(xmlString)
     
   chan = tree.find('channel')
   
   item = ET.SubElement(chan, 'item')
   
   #add subinfor for item
   title = ET.SubElement(item, 'title')
   title.text = xmlItem['title']
   
   author = ET.SubElement(item, 'ns0:author')
   author.text = xmlItem['author']

   summary = ET.SubElement(item, 'ns0:summary')
   summary.text = xmlItem['description']

   subtitle = ET.SubElement(item, 'subtitle')
   subtitle.text = xmlItem['subtitle']

   description = ET.SubElement(item, 'description')
   description.text = xmlItem['description']

   #TODO guid
   guid = ET.SubElement(item, 'guid')
   guid.text = xmlItem['guid']

   #TODO Find full audio web url
   audio_web_url = webUrl + rss_url +'/'+ audio_filename

   #TODO Find length of audio file -- should we do this in php when adding to database?
   length = 2000000
   enclosure = ET.SubElement(item, 'enclosure')
   enclosure.set('url', audio_web_url)
   enclosure.set('length', str(length))
   enclosure.set('type', 'audio/x-mp3')

   pubDate = ET.SubElement(item, 'pubDate')
   pubDate.text = xmlItem['pubDate']

   duration = ET.SubElement(item, 'ns0:duration')
   duration.text = str(length)


   xmlString = ET.tostring(tree)
   xmlString.replace('><', '>\n<')

   print xmlString

  #overwrite old file
   with open(xmlFileUrl, 'w') as xmlFile:
       xmlFile.write('''<?xml version="1.0" encoding="UTF-8"?>''')
       xmlFile.write(xmlString)


if __name__ == '__main__':
    try:
        rss_url = argv[1]
        audio_filename = argv[2]
        itemXMLData_json_str = argv[3]
        xmlItem = json.loads(itemXMLData_json_str)

        updatePodcastXml(rss_url, audio_filename, xmlItem)
    except:
        logging.exception('In file, '+ argv[0] +', json: '+itemXMLData_json_str+', exception:')

