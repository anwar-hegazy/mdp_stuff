"""Notes for web scraping (Spring 2013, ACCD)
inspired by this lecture: https://www.youtube.com/watch?v=52wxGESwQSA

Note: you should be setup with the following tools/platforms:
    MacPorts, Pip, iPython (see here for a refresher:
    http://www.caseythomasanderson.com/teaching/intro-to-programming/),
    and a Text Editor, (like Sublime Text or Text Mate) 

Good tools:
Firebug or Chrome DOM Inspector
    You will use these to look for patterns on web pages which you can use
    to computationally explore/manipulate/interact with parts of the page

Python modules:
    lxml, requests, mechanize, BeautifulSou

    we can get these via pip (in the terminal):
        -to search for a package (BeautifulSoup example):
        /opt/local/bin/pip-2.7 search BeautifulSoup
        
        -to install the package:
        sudo /opt/local/bin/pip-2.7 install BeautifulSoup

Remember: The idea here is to use web scraping techniques as an alternative to
a supported API. Consider this a proof of concept that you do not HAVE to find an
API for a web service to computationally explore the web.
"""

"""Here is our sample program, courtesy of Asheesh Laroia (seriously, that video I linked to above is awesome).
I have altered this slightly from his version, but we will change it quite a bit throughout the hour"""

#search google
import requests
import urllib
import lxml.html

GOOGLE_BASE='http://google.com/search?q='
search_term = input('Enter the search term (strings must have quotes): ')   #added by CTA

def search_for(s):
    page_text = requests.get(GOOGLE_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect('cite')
    first_url = urls[0]
    return first_url.text_content()

if __name__ == '__main__':
    print search_for(search_term)

""""Requests is an HTTP library for Python. While Python has a built in module for getting
things from the web (urllib and urllib2), Requests makes exploring the information you
scrape from websites easier to manipulate"""

#Let's break this down line by line
#First we import the libraries we want to use:
import requests
import urllib
import lxml.html

#then we declare a variable that will store the basic google search path
GOOGLE_BASE='http://google.com/search?q='

"""In an effort to make this more compact, i have included a line that will allow me to
type whatever term i want into the command line and pass that to the function search_for"""

search_term = input('Enter the search term (strings must have quotes): ')

#if you now execute search_term, you will get whatever we just typed into the command line

#the function search_for(s) does all of the work for us, but lets go ahead and explore it
#i will replace the placeholder 's' with search_term (otherwise this will not work by itself)
page_text = requests.get(GOOGLE_BASE + urllib.quote(search_term)).text

#run that, and then go ahead and do this:
page_text

#awesome. we get a huge mess. let's start by seeing what type of data we have in page_text

type(page_text)

"""returns unicode. fine. if you type page_text. and then hit the tab key you can see all the
methods we get from a unicode object after calling requests.get on it"""

#page_text.#[TAB]

#returns something like this
""""
page_text.capitalize  page_text.isalnum     page_text.ljust       page_text.rstrip
page_text.center      page_text.isalpha     page_text.lower       page_text.split
page_text.count       page_text.isdecimal   page_text.lstrip      page_text.splitlines
page_text.decode      page_text.isdigit     page_text.partition   page_text.startswith
page_text.encode      page_text.islower     page_text.replace     page_text.strip
page_text.endswith    page_text.isnumeric   page_text.rfind       page_text.swapcase
page_text.expandtabs  page_text.isspace     page_text.rindex      page_text.title
page_text.find        page_text.istitle     page_text.rjust       page_text.translate
page_text.format      page_text.isupper     page_text.rpartition  page_text.upper
page_text.index       page_text.join        page_text.rsplit      page_text.zfill"""


#so, if you do not know what any of these do, it is as simple as typing the variable.method and
#then a question mark

page_text.find?

#you can explore all of the functions provided by page_text this way

""""in order to explore what our request call brought back, let's parse it using lxml.html"""

parsed = lxml.html.fromstring(page_text)

"""lxml is a module for parsing xml, in case that was unclear. xml is considered old-fashioned,
but it is still used all over the web, so this is a pretty handy module for exploring text on a web-page"""

#try this
type(parsed)

#which returns
lxml.html.HtmlElement

#okay fine, lets now try this
parsed

#which simply confirms that it is an htmlelement, so we are going to have to dig a little deeper

#now do this
#parsed.#[tab]

#which returns
"""parsed.addnext              parsed.get_element_by_id    parsed.keys
parsed.addprevious          parsed.getchildren          parsed.label
parsed.append               parsed.getiterator          parsed.make_links_absolute
parsed.attrib               parsed.getnext              parsed.makeelement
parsed.base                 parsed.getparent            parsed.nsmap
parsed.base_url             parsed.getprevious          parsed.prefix
parsed.body                 parsed.getroottree          parsed.remove
parsed.clear                parsed.head                 parsed.replace
parsed.cssselect            parsed.index                parsed.resolve_base_href
parsed.drop_tag             parsed.insert               parsed.rewrite_links
parsed.drop_tree            parsed.items                parsed.set
parsed.extend               parsed.iter                 parsed.sourceline
parsed.find                 parsed.iterancestors        parsed.tag
parsed.find_class           parsed.iterchildren         parsed.tail
parsed.find_rel_links       parsed.iterdescendants      parsed.text
parsed.findall              parsed.iterfind             parsed.text_content
parsed.findtext             parsed.iterlinks            parsed.values
parsed.forms                parsed.itersiblings         parsed.xpath
parsed.get                  parsed.itertext             """

#try typing any of those methods followed by a question mark for a description of what it does

#example:
parsed.cssselect?

#returns
""""Type:       instancemethod
String Form:<bound method HtmlElement.cssselect of <Element html at 0x10a4cd650>>
File:       /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/lxml/html/__init__.py
Definition: parsed.cssselect(self, expr, translator='html')
Docstring:
Run the CSS expression on this element and its children,
returning a list of the results.

Equivalent to lxml.cssselect.CSSSelect(expr, translator='html')(self)
-- note that pre-compiling the expression can provide a substantial
speedup."""

""""if we search by a known tag (the example above looks for cite), and parse based on that,
we can return information attached to that element. 'cite' should give us the title of whatever returned,
but we could always look around in the DOM inspector to see what else might be worth trying.
note: to explore stuff on the web, some guessing may be necessary, as you cannot expect all html to respect
web standards (etc.)"""

#try this:
urls = parsed.cssselect('cite')

#which returns a list of urls. perfect. lets look at each element
urls[0].text_content()

#which shows me the top google result for the search_term 'whateverwetyped'

#cool. what if we want to see ALL of the urls? we could do this

for i in range(len( urls ) ):
    print "result # " + str( i ) + ': ' + str( urls[i].text_content() )

#returns this (if you search for 'casey'):
""""result # en.wikipedia.org/wiki/Casey
result #0: www.yelp.com/biz/caseys-irish-pub-los-angeles-3
result #1: 213nightlife.com/caseysirishpub
result #2: www.caseys.com/
result #3: www.caseyscupcake.com/
result #4: www.casey.senate.gov/
result #5: www.casey.org/
result #6: www.bvsd.org/schools/casey/Pages/default.aspx
result #7: www.caseyreinhardt.com/
result #8: www.caseyresearch.com/
result #9: NBCSports.com
result #:10 CBS Local"""

"""that object up there is set up to simply return the top result for whatever search term you enter,
so now try running the entire program"""

import requests
import urllib
import lxml.html

GOOGLE_BASE='http://google.com/search?q='
search_term = input('Enter the search term (strings must have quotes): ')

def search_for(s):
    page_text = requests.get(GOOGLE_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect('cite')
    first_url = urls[0]
    return first_url.text_content()

if __name__ == '__main__':
    print search_for(search_term)

#and with a simple change, we can return the first however many results. try this:

import requests
import urllib
import lxml.html

GOOGLE_BASE='http://google.com/search?q='
search_term = input('Enter the search term (strings must have quotes): ')

def search_for(s):
    rslts = []
    page_text = requests.get(GOOGLE_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect('cite')
    print 'found ' + str( len( urls ) ) + ' results!'
    for i in range( len( urls ) ):
        rslts.append( urls[i].text_content() )
    return rslts

if __name__ == '__main__':
    print search_for(search_term)       

"""in order to write the results to a variable that can be accessible outside of this function, get rid of the
if __name__ blah blah, delete the line that starts with 'search_term', and then do this:"""

#it should look like this now:
import requests
import urllib
import lxml.html

GOOGLE_BASE='http://google.com/search?q='

def search_for(s):
    rslts = []
    page_text = requests.get(GOOGLE_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect('cite')
    print 'found ' + str( len( urls ) ) + ' results!'
    for i in range( len( urls ) ):
        rslts.append( urls[i].text_content() )
    return rslts


"""put this code in its own file (saved as a .py), then cd to that dir
"""

cd Desktop/SCRAPING/
ls
#returns:
google_search_any_field.py	simple_google_cmndln_input.py
google_search_any_field.pyc	web_scraping_lecture.py
google_search_return_all.py	yahoo_asheesh.py
google_yahoo_search_with_if.py	yahoo_search_doesntwork_poc.py
google_yahoo_two_objects.py

#go back into ipython and %run that file
%run search_requests_google_v2.py

#which, because i put that input line in there, will run the function once (take that out if this is annoying to you)
#then, write the returned results to a variable
search = search_for('terrorism')
search

#returns:
"""['en.wikipedia.org/wiki/Terrorism',
 'www.fbi.gov/about-us/investigate/terrorism',
 'www.merriam-webster.com/dictionary/terrorism',
 'dictionary.reference.com/browse/terrorism',
 'www.cfr.org/issue/135/',
 'www.un.org/terrorism/',
 'www.terrorism-research.com/',
 'www.fas.org/irp/threat/terror.htm',
 'www.start.umd.edu/gtd/',
 'www.satp.org/satporgtp/terrorism.asp',
 'The Guardian',
 'The News International',
 'Reuters Blogs (blog)']"""

"""so, if we wanted to just have a general tool for grabbing info from google, we could
make a new file that looks likes this (in the same dir):"""

import requests
import urllib
import lxml.html

GOOGLE_BASE='http://google.com/search?q='

def search_for(s, css):
    rslts = []
    page_text = requests.get(GOOGLE_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect(str( css ) )
    print 'found ' + str( len( urls ) ) + ' results!'
    for i in range( len( urls ) ):
        rslts.append( urls[i].text_content() )
    return rslts     


"""so ive added a second parameter, enabling me to get whatever element
i want to parse for. here is a proof of concept (i.e. repeating what we did above with our new format)"""

#this next line imports the function from that file
from google_search_any_field import*
search = search_for('terrorism', 'cite')
#returns:
found 13 results!

#now lets see what we got:
search
#returns
""""['en.wikipedia.org/wiki/Terrorism',
 'www.fbi.gov/about-us/investigate/terrorism',
 'www.merriam-webster.com/dictionary/terrorism',
 'dictionary.reference.com/browse/terrorism',
 'www.cfr.org/issue/135/',
 'www.un.org/terrorism/',
 'www.terrorism-research.com/',
 'www.fas.org/irp/threat/terror.htm',
 'www.start.umd.edu/gtd/',
 'www.satp.org/satporgtp/terrorism.asp',
 'The Guardian',
 'The News International',
 'Reuters Blogs (blog)']"""


#great, lets try the same word, but search by the element 'a' (which should return every single link on that page)
search = search_for('terrorism', 'a')
#returns
found 95 results!

#wow. this is going to be a lot of garbage (i bet).
#to see what we got, simply do this:
a

"""so, that returns everything on the google page, including stuff that has nothing to do with our search term
hopefully it now makes sense why it is more relevant to us to search for 'cite', which will give us the title source
for each element on the list"""

"""so far we have only been looking at google results. what if we wanted to compare the results from, say, Yahoo and Google?"""

#remember, this variable was the basis for our search queries
GOOGLE_BASE='http://google.com/search?q='

#let's say that we wanted to compare search engine results. make a new file with this:
import requests
import urllib
import lxml.html

#GOOGLE_BASE='http://google.com/search?q='
YAHOO_BASE='http://search.yahoo.com/search?p='

def search_for(s, el):
    rslts = []
    page_text = requests.get(YAHOO_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect(str( el ) )
    print 'found ' + str( len( urls ) ) + ' results!'
    for i in range( len( urls ) ):
        rslts.append( urls[i].text_content() )
    return rslts        


""""when i run this, it returns 2 results, which does not really seem correct to me (after all, google
returned at least ten). we can confirm that our script above does not totally work correctly by comparing
what is returned by the function to a simple search via the yahoo page (i.e. in the browser). when i did this,
the search returned roughly ten or so results. after some research, it became clear that yahoo handles search
requests differently than google. here is how the guy from the video at the beginning of this page scrapes
information from yahoo (though ive changed his code to show all results on the first page)"""

import requests
import urllib
import lxml.html

YAHOO_BASE='http://search.yahoo.com/search?p='

def search_for(s):
    rslts = []
    page_text = requests.get(YAHOO_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect('.url')
    print 'found ' + str( len( urls ) ) + ' results!'
    for i in range( len( urls ) ):
        rslts.append( urls[i].text_content() )
    return rslts


#notice the differences between this version and the google version.
#google version:
parsed = lxml.html.fromstring(page_text)
urls = parsed.cssselect('cite')
 
#yahoo version:
parsed = lxml.html.fromstring(page_text)
urls = parsed.cssselect('.url')

""""so, we have two options here: 1. use separate objects for each search engine. 2. add an if statement
that checks to see which search engine we want to look at, and makes the appropriate changes to our code.
on the one hand, it would not take much to add this if statement. on the other hand, if we did so for every
search engine that we wanted to compare, our nice, compact object would get much longer. this is really
a matter of personal preference, so here are both versions"""

#google and yahoo in the same file
import requests
import urllib
import lxml.html

GOOGLE_BASE='http://google.com/search?q='
YAHOO_BASE='http://search.yahoo.com/search?p='

def google_search_for(s):
    rslts = []
    page_text = requests.get(GOOGLE_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect('cite')
    print 'found ' + str( len( urls ) ) + ' results!'
    for i in range( len( urls ) ):
        rslts.append( urls[i].text_content() )
    return rslts

def yahoo_search_for(s):
    rslts = []
    page_text = requests.get(YAHOO_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = parsed.cssselect('.url')
    print 'found ' + str( len( urls ) ) + ' results!'
    for i in range( len( urls ) ):
        rslts.append( urls[i].text_content() )
    return rslts

#OR, with a test
import requests
import urllib
import lxml.html

GOOGLE_BASE='http://google.com/search?q='
YAHOO_BASE='http://search.yahoo.com/search?p='

def search_for( s, base ):
    rslts = []
    if base == 'google':
        page_text = requests.get(GOOGLE_BASE + urllib.quote(s)).text
        parsed = lxml.html.fromstring(page_text)
        urls = parsed.cssselect('cite')
    elif base == 'yahoo':
        page_text = requests.get(YAHOO_BASE + urllib.quote(s)).text
        parsed = lxml.html.fromstring(page_text)
        urls = parsed.cssselect('.url')

    print 'found ' + str( len( urls ) ) + ' results!'
    for i in range( len( urls ) ):
        rslts.append( urls[i].text_content() )
    return rslts

#assignment: how would you add bing search results to this?