import xml.etree.ElementTree as ET
import json
from sys import argv

webUrl = 'http://75.39.13.254/podcasts'
#webUrl = 'http://ec2-54-226-137-31.compute-1.amazonaws.com/podcasts'

site_dir = '/vagrant/website'
#site_dir = '/var/www'

def updatePodcastXml(rss_url, title, audio_filename, pubDate):
   # load current xml file

   with open(site_dir+'/podcasts/argsout.txt', 'w') as argsoutFile:
     argsoutFile.write(str(rss_url)+'\n')
     argsoutFile.write(str(title)+'\n')
     argsoutFile.write(str(audio_filename)+'\n')
     argsoutFile.write(str(pubDate)+'\n')

   xmlFileUrl = site_dir+'/podcasts/' + rss_url +'/podcast.xml'
   xmlString = ''
   with open(xmlFileUrl, 'r') as xmlFile:
     xmlString=''.join([line for line in xmlFile])

     tree = ET.fromstring(xmlString)
     
     chan = tree.find('channel')
     
     item = ET.SubElement(chan, 'item')
     
     #add subinfor for item
     it_title = ET.SubElement(item, 'title')
     it_title.text = title
     
     #TODO Find full audio web url
     audio_web_url = webUrl +'/'+ rss_url +'/'+ audio_filename

     #TODO Find length of audio file -- should we do this in php when adding to database?
     it_enclosure = ET.SubElement(item, 'enclosure', {'url':audio_web_url, 'length':"2000000",
                                                      'type':'audio/x-mp3'})
     #TODO guid
     
     if pubDate: 
        it_pubDate = ET.SubElement(item, 'pubDate')
        it_pubDate.text = pubDate

     xmlString  = ET.tostring(tree)

   print xmlString
  #overwrite old file
   with open(xmlFileUrl, 'w') as xmlFile:
     xmlFile.write(xmlString)

if __name__ == '__main__':
    #x = open('/', 'w')
    #x.write('ha')
    #x.close()
    rss_url = argv[1]
    title = argv[2]
    audio_filename = argv[3]
    if len(argv) > 4:
        pubDate = argv[4]
    else:
        pubDate = None
    updatePodcastXml(rss_url, title, audio_filename, pubDate)

