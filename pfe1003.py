print("Chapter 10: Exercise 3")

#imports the string we need to do deletions later
import string

fname = input("Please provide a text file name:")

#try to open text file
try:
    fopen = open(fname)

except:
    print('File cannot be opened:', fname)
    exit()

#this creaes the dictionary
mailcount = {}

#for each line in the file delete the punctuation and digits then lower the caps and split into a list
#second for loop takes the strings in the list and for each word makes a new list of each letter in the word
#third for loop takes each letter and uses get to either add it to the dictionary with 0 as the value or add 1 to the value if it exists
for line in fopen:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    line = line.split()
    for word in line:
        letters = list(word)
        for letter in letters:
            mailcount[letter] = mailcount.get(letter,0) + 1

#check mailcount prints correctly
#print(mailcount)

#maillist is a list that will take the tubles and sort them by letter

maillist = []
for key, val in list(mailcount.items()):
    maillist.append((key,val))

#this prints out the sorted list of tuples
maillist.sort()
print("Sorted list", maillist)

#this code grabs each tuple and prints them out sequentially by letter

for letter, count in maillist:
    print(letter, count)
