
from goose import Goose
from sys import argv 
from updatePodcastWithDatabase import site_dir
import json
import urllib2
import logging

# set up logging errors
logging.basicConfig(level=logging.DEBUG, filename='/vagrant/wulu_errors.log')



def getArticleTextFromGoose(url):
    
    g = Goose()

# NOTE, on error this will return ''. Caller should check for this
# and not try to text-to-speech it.
    cleanText=''
    try:
        cleanText=g.extract(url).cleaned_text
    except ValueError, e:
        #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        #response = opener.open(url)
        
        #raw_html = response.read()
        #utf8_str = unicode(raw_html, 'utf-8')

        #a = g.extract(raw_html=utf8_str)

        pass

    cleanText=cleanText.strip(' \t\n\r')

# Some websites need cookies to read them (eg NYTimes).
# If reading fails, try again with cookies
    if (cleanText == ''):
        try:
            print "EMPTY CLEAN TEXT"
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
            print "url:", url
            response = opener.open(url)
            
            raw_html = response.read()
            a = g.extract(raw_html=raw_html)
            cleanText = a.cleaned_text
        except:
            pass


    return cleanText

def getArticleTextFromReadability(url):
    ''' If Goose didn't work, let's try this other lib.'''
    from readability.readability import Document
    import urllib
    import nltk 
    
    html = urllib.urlopen(url).read()
    cleanHtml = Document(html).summary()
    cleanText = nltk.clean_html(cleanHtml)
    return cleanText


if __name__ == "__main__":
    cleantext = ''
    try: 
        cleantext = getArticleTextFromGoose(argv[1])
    except:
        logging.exception('In file, '+ argv[0] +', opening, "'+argv[1]+'", exception. argv: '+str(argv))

    try:
        if not cleantext:
            print 'trying readability'
            cleantext = getArticleTextFromReadability(argv[1])
    except:
        logging.exception('In file, '+ argv[0] +', opening, "'+argv[1]+'", exception. argv: '+str(argv))

    print json.dumps(cleantext)

