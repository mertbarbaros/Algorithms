"""
ASCII order
"""

print("Order of H is: ",ord('H'))
print("Order of e is: ", ord('e'))
print("Order of a new line is: ", ord('\n'))

"""
URLLIB
"""
import urllib.request, urllib.error, urllib.parse

fhand = urllib.request.urlopen('https://barbaros.blog/about')

for line in fhand:
    print(line.decode().strip())
    
"""
URLLIB EXAMPLE
"""

import urllib.request, urllib.error, urllib.parse

#open the file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

    
#let's count the words
    
counts = dict()

for line in fhand:
    words = line.decode().strip()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)

"""
Beautiful Soup
"""

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input("Enter -: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrive all of the anchor tags
tags = soup('a')

for tag in tags:
    print(tag.get('href', None))
    
"""
Working With SSL sites
"""
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open
url = input("Enter -: ")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrive all of the anchor tags
tags = soup('a')

for tag in tags:
    print(tag.get('href', None))

"""
Span Tags
http://py4e-data.dr-chuck.net/comments_685221.html
"""
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open
url = input("Enter -: ")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

summ = 0
tags = soup('span')

for tag in tags:
    summ = summ + int(tag.contents[0])

print(summ)

"""
example
"""

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

#url = 'http://py4e-data.dr-chuck.net/known_by_Happy.html'
url = input("Enter -: ")
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')


for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
