
#Similar reference files: Urllib and Requests.py. Contains urllib and requests module

import urllib.request, urllib.response, urllib.parse, urllib.error

#Alternatively:
#from urllib import request, response, parse, error

address = "http://data.pr4e.org/romeo.txt"      #NB: Address can be either a file on the webpage or the webpage itself
response = urllib.request.urlopen(address)
for content in response:
    print(content.decode().strip())


#================ WEB SCRAPING(or SPIDERING or WEB CRAWLING =============
'''
Web scraping is the act of retrieving a web page, extracting and using information from that web page
A module good for this is "Beautiful soup.
'''
