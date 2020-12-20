print('Chapter 11: Exercise 1')


#Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

#import regular expressions
import re

#Code to save time
#mbox = 'mbox-short.txt'
#Prompt for file and expression you want to search for and set-up a list
fname = input('Please provide a text file name:' )
rname = input('Please provide a regular expression:')
rlist = []


#try to open the file
try:
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip()
        rfind = re.findall(rname, line)
        if len(rfind) > 0:
            #Test expression finding worked
            #print(rfind)
            rlist.append(rfind)

except:
    print('File cannot be opened:', fname)

#test list that items from file were found and added to list
#print(rlist)
#print(len(rlist))

#print out the total lines that matched the expression in the file
print(fname, 'had a total of', len(rlist), 'lines that matched', rname)
