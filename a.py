from bs4 import BeautifulSoup
import requests
import urllib2
import re
#import b

#for x in list1:
#	print x

#url=x
url = 'https://allevents.in/new%20delhi/expressionism-art-workshop-2017/80006190664762'
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
	adrrr=adrr.lstrip()
	print "Address:- ", adrrr

 
# Fetch Organizer name


for adr in soup.findAll("div", { "class" : "name" }):
 
	
	orginazer = adr.find('span')

	print orginazer.text.lstrip()

# Fetch follower count
for adr in soup.findAll("div", { "class" : "detail" }):
 
	
	orginazer = adr.find('span')

	
	print orginazer.text
# Fetch evnt count
for adr in soup.findAll("div", { "class" : "detail" }):
 
	r = adr.findAll('span')

	
	print r[2].text
# decription

r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')

for adr in soup.findAll("div", { "property" : "schema:description" }):
 
	
	

	print ("Decription")
	dec= adr.text
	print dec.lstrip(" ")
	
#fetch latitude and longitude


from geopy.geocoders import Nominatim
geolocator = Nominatim()


location = geolocator.geocode(adrr)
#print(location.address)
print((location.latitude, location.longitude))


