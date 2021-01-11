print('Chapter 11: Finding Numbers in a Haystack')
#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re

sample = 'regex_sum_42.txt'
actual = 'regex_sum_1119254.txt'

fname = input('Please provide a text file name to open:')
sumlist = list()
sumtotal = 0

try:
    fopen = open(fname)
    for line in fopen:
        line = line.rstrip()
        rfind = re.findall('[0-9]+', line)
        sumlist.extend(rfind)

    for string in sumlist:
        floatpoint = float(string)
        sumtotal = sumtotal + floatpoint

    print(sumtotal)
except:
    print('An error occured while opening the file')
