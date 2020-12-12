print("Chapter 8: Exercise 3")
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) > 1 and words[0] == 'From':
        print(words[2])
