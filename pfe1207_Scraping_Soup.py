print('Chapter 12: Scraping Numbers from HTML using Beautiful Soup')
#In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
sample = 'http://py4e-data.dr-chuck.net/comments_42.html'
actual = 'http://py4e-data.dr-chuck.net/comments_1119256.html'

count = 0
spansum = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    count = count + 1
    spansum = spansum + float(tag.contents[0])
    #print('Span', tag.contents[0])

print('Count', count)
print('Sum', spansum)
