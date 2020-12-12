print("Chapter 8: Exercise 2")
fhand = open('mbox-short2.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if len(words) < 2 : continue
    print(words[2])


print ("The code would still fail if you have a line that starts with From but has no other words in the line, a new guardian code was written to check to make sure the line was greater than 2 in length of words")
