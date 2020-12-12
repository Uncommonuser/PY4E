print ("Chapter 7: Exercise 2")
count = 0
total = 0

filename = input("Please provide a file name:")
if filename == 'easter':
    print("You have found an easter egg!")
    quit()
else:
    try:
        fileopen = open(filename)
    except:
        print(filename, 'could not be opened, or is not a file')
        quit()

for line in fileopen:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        total = total + float(line.lstrip("X-DSPAM-Confidence:"))

print('There were', count, 'lines with spam confidence detectors', 'with a total spam confidence value of', total, 'and average spam confidence value of', total/count)
