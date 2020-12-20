print('Chapter 11: Exercise 2')


#Write a program to look for lines of the form
#`New Revision: 39772`
# and extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average.

#import regular expressions
import re

#Code to save time
#fname = 'mbox-short.txt'
fname = input('Please provide a text file name:' )

rlist = []


#try to open the file
try:
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip()
        #find all lines that contain 'New Revision: followed by any number of characters and a whitespace before numbers begin. Just extract the integers.
        rfind = re.findall('New Revision:.*\s([0-9.]+)', line)
        if len(rfind) > 0:
            #Test expression finding worked
            #print(rfind)
            #findall extracts the numbers as a string and stores them as a list in rfind so you have to float it and identify the index which is 0 cause its a list of 1 before you store it in rlist so that you can sum it later. .
            rfind = float(rfind[0])
            rlist.append(rfind)

except:
    print('File cannot be opened:', fname)

#test list that items from file were found and added to list and that len and sum work
#print(rlist)
#print(len(rlist))
#print(sum(rlist))


#print out the total lines that matched the expression in the file
print(fname, 'has an average of', sum(rlist)/len(rlist))
