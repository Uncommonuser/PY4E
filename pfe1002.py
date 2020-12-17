print("Chapter 10: Exercise 2")

fname = input("Please provide a text file name:")

#try to open text file
try:
    fopen = open(fname)

except:
    print('File cannot be opened:', fname)
    exit()

#mailcount is a dictionary that will grab the hour as the first split of the sixth word from each line that starts with 'From'
mailcount = {}
for line in fopen:
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        hour = words[5]
        hour = hour.split(":")
        mailcount[hour[0]] = mailcount.get(hour[0],0) + 1

#check mailcount prints correctly
#print(mailcount)

#maillist is a list that will take the hours and counts from mailcount and add them in as tuples #then sort so smallest hour is first

maillist = []
for key, val in list(mailcount.items()):
    maillist.append((key,val))

maillist.sort()
print("Sorted list", maillist)

#this code grabs each tuple and prints them out sequentially

for hour, count in maillist:
    print(hour, count)
