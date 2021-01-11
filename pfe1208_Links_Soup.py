print('Chapter 12: Following Links in Python')
#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

sample = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
actual = 'http://py4e-data.dr-chuck.net/known_by_Coco.html'

namelist = []

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#code to test sample url
#count = 4
#position = 3
#url = sample

url = input('Enter - ')
count = input('Enter count: ', )
count = int(count)
position = input('Enter position: ', )
position = int(position)



# Retrieve all of the anchor tags
for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    poscounter = 0
    for tag in tags:
        poscounter = poscounter + 1
        if poscounter == position:
            url = tag.get('href', None)
            #print(tag.get('href', None))
            namelist.append(tag.contents[0])
            #print(tag.contents[0])

print('Finding the link at position', position, 'and repeating', count, 'times')
print('The list of names is:', namelist)
