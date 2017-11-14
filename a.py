from bs4 import BeautifulSoup
import requests
import urllib2
import re
import b



url=x
#url = 'https://allevents.in/new%20delhi/run-for-laadli-a-unique-half-marathon-by-delhi-police/1775805199104598#'
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

# Fetch title

title=soup.title.string
print "Title:- ", title

#Fetch time and date

response = urllib2.urlopen(url)
page = response.read()
p = page
m = re.findall(r'[a-z]{3} [a-z]{3} [0-9]{1,2} [0-9]{4} at [0-9]{2}:[0-9]{2} [a-z]{2}',p,re.I|re.M)

print "Date and Time :- " ,m[1]

#Fetch Address

for adr in soup.findAll("div", { "class" : "pd-lr-10 span9" }):
 
	adrr = adr.find('li', 'toh venue-li').contents[2]

	print "Address:- ", adrr.lstrip()

# Fetch Organizer name

#url = 'https://allevents.in/ahmedabad/rann-utsav-2017-18/2119131864779416#'

r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
# Fetch Organizer name
"""for adr in soup.findAll("div", { "class" : "name" }):
 
	
	#orginazer = adr.find('span')
	#print orginazer.split('\n')
	#org = orginazer.text.lstrip()
	#print "orgnizer:- ", org """

# Fetch follower count
for adr in soup.findAll("div", { "class" : "detail" }):
 
	
	orginazer = adr.find('span')

	
	print orginazer.text
# Fetch evnt count
for adr in soup.findAll("div", { "class" : "detail" }):
 
	r = adr.findAll('span')

	
	print r[2].text


