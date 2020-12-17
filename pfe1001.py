print("Chapter 10: Exercise 1")

fname = input("Please provide a text file name:")
#try to open text file
try:
    fopen = open(fname)

except:
    print('File cannot be opened:', fname)
    exit()

#mailcount is a dictionary that will grab any email addresses as the second word from each line that starts with 'From'
mailcount = {}
for line in fopen:
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        mailcount[words[1]] = mailcount.get(words[1],0) + 1

print(mailcount)

#maillist is a list that will take the emails and counts from mailcount and add them in as tuples in reverse order (email/count to count/email)
#then sort in reverse order so largest is first

maillist = []
for key, val in list(mailcount.items()):
    maillist.append((val,key))

maillist.sort(reverse=True)

#this code grabs the first tuple in maillist using split and prints them in reverse making it email/count again
for count, address in maillist [:1]:
    print(address, count)
