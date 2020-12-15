print("Chapter 9: Exercise 3")

fname = input("Please provide a text file name:")
try:
    fopen = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


mailcount = {}
for line in fopen:
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        mailcount[words[1]] = mailcount.get(words[1],0) + 1

print(mailcount)
