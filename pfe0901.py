print("Chapter 9: Exercise 1")

wordlist = open('mbox-short.txt')
dict = {}
print("Dictionary originally contained:", dict)

for line in wordlist:
    words = line.split()
    for word in words:
        dict[word] = 0

print("length of dictionary", len(dict))
print('From', 'From' in dict)
print('Terrible', 'Terrible' in dict)
