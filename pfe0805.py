print('Chapter 8: Exercise 5')

eput = input("Please provide text file:", )
count = 0

try:
    eopen = open(eput)
    for line in eopen:
        words = line.split()
        if len(words) > 1 and words[0] == 'From':
            print(words[1])
            count = count + 1
except:
    print("The file name you provided was not valid")
    




print("There were", count, "lines in the file with From as the first word and that contained an email address")
