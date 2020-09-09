

In this assignment you will write a Python program somewhat similar to 
http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read 
the XML data from that URL using urllib and then parse and extract the comment
 counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give
you the sum for your testing and the other is the actual data you need to
process for the assignment.

Actual data: http://py4e-data.dr-chuck.net/comments_752625.xml 
(Sum ends with 75)
You do not need to save these files to your folder since your program will
read the data directly from the URL. Note: Each student will have a distinct
data url for the assignment - so only use your own data url for analysis.
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open the url
url = 'http://py4e-data.dr-chuck.net/comments_752625.xml'
xml = urllib.request.urlopen(url, context= ctx)
data = xml.read()

tree = ET.fromstring(data)
total = 0

for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        total += int(comment.find('count').text)
        
print(total)
