from bs4 import BeautifulSoup
import requests
import urllib2
import re



import requests
from BeautifulSoup import BeautifulSoup
url = "https://allevents.in/new%20delhi/all#"
response = requests.get(url)
page = str(BeautifulSoup(response.content))

def getURL(page):
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"https://allevents.in/new%20delhi/', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

list1=[]
while True:
    url, n = getURL(page)
    page = page[n:]
    if url != "https://allevents.in/new%20delhi/all":
       # print url
	list1.append(url)
    else:
        break
	f.close()
# fetch urls from start url
length=len(list1)
print ("number of urls:-"),length

for url in list1:
	#print url
