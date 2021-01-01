print('Chapter 12: Exercise 3')
#Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
#Notes: This is after reading someone elses code, much better

import urllib.request

inputURL = input('Please provide a website URL: ',)
#lazy code check inputURL = 'http://data.pr4e.org/romeo.txt'


try:
    openURL = urllib.request.urlopen(inputURL).read()
    print('URL successfully opened')

except:
    print('Sorry, bad URL')

decodeURL = openURL.decode()
count = len(decodeURL)
print('The total characters in', inputURL, 'is', count)
print(decodeURL[:3000])
