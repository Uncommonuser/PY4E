print('Chapter 13: Extracting Data from JSON')


#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
import urllib.request, urllib.parse, urllib.error
import json
import ssl

sample = ' http://py4e-data.dr-chuck.net/comments_42.json'
actual = 'http://py4e-data.dr-chuck.net/comments_1119259.json'

inputURL = input('Please provide a website URL: ',)
#inputURL = sample
#inputURL = actual

uh = urllib.request.urlopen(inputURL)
data = uh.read().decode()

info = json.loads(data)
#print(type(info))
#print(info)
#print('User count:', len(info))
#print(info.keys())
openinfo = info['comments']
#print(type(openinfo))
#print(type(openinfo[0]))

sum = 0

for number in openinfo:
    sum = int(number['count']) + sum

print('Count', len(openinfo))
print('Sum', sum)
