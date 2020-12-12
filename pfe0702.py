print ("Chapter 7: Exercise 2")
count = 0
total = 0

filename = input("Please provide a file name:")
try:
    fileopen=open(filename)
except:
    print('File cannot be opened', filename)
    quit()
for line in fileopen:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        total = total + float(line.lstrip("X-DSPAM-Confidence:"))

print('There were', count, 'lines with spam confidence detectors', 'with a total spam confidence value of', total, 'and average spam confidence value of', total/count)
