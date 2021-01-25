print('Chapter 13: Extracting Data from XML')


#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sample = ' http://py4e-data.dr-chuck.net/comments_42.xml'
actual = 'http://py4e-data.dr-chuck.net/comments_1119258.xml'

inputURL = input('Please provide a website URL: ',)
#inputURL = sample
#inputURL = actual

openURL = urllib.request.urlopen(inputURL).read()
print('URL successfully opened', type(openURL))

data = openURL
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

results = tree.findall('.//count')

print('Total items counted', len(results))
#print('results type', type(results))

sum = 0
for numbers in results:
    sum = int(numbers.text) + sum
    #print(item.text)
    #print(type(item.text))


print('Sum is:', sum)

#The following two loops are just looking to find different ways to print out the information from the URL and practice XML more
#results2 = tree.findall('comments/comment/name')
#print('Names count 2', len(results2))

#namelist = []
#for names in results2:
    #namelist.append(names.text)
#print(namelist)

#results3 = tree.findall('comments/comment')
#for item in results3:
    #print(item.find('count').text)
    #print(item.find('name').text)
