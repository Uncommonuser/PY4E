print('Chapter 12: Exercise 3')
#Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
#Notes: The output is kind of ugly, need to figure out how to preserve original text spacing

import urllib.request

inputURL = input('Please provide a website URL: ',)
#lazy code check inputURL = 'http://data.pr4e.org/romeo.txt'

#set up count for char count and empty list for building print out
count = 0
urllist = []

#try to open URL, loop through each line then each word use list() to create list of letters in word
#use len() to add characters of each word to count
#use if/else statement to append words to list as long as count of chars is less than 3000, else just count up chars
try:
    openURL = urllib.request.urlopen(inputURL)
    print('URL successfully opened')
    for line in openURL:
        words = line.decode().split()
        #print(words)
        for word in words:
            #print(letters)
            letters = list(word)
            if count < 3000:
                count = count + len(letters)
                urllist.append(word)
                #print(len(letters))
            else:
                count = count + len(letters)



except:
    print('Sorry, bad URL')

#use join to join the list into one string with spaces joining them as denoted by ' ', if '-' then-join-words-this-way
stringlist = ' '.join(urllist)
print(stringlist)
print('The total characters in', inputURL, 'is', count)
