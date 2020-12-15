print("Chapter 9: Exercise 2")

fname = input("Please provide a text file name:")
try:
    fopen = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


weekcount = {}
for line in fopen:
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        weekcount[words[2]] = weekcount.get(words[2],0) + 1

print(weekcount)
