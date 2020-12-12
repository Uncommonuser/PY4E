print ("Chapter 6: Exercise 5")

str = 'X-DSPAM-Confidence:0.8475'

print(str.find(':'))
slice = str.find(':')
print(str[slice+1:])
number = float(str[slice+1:])
print(number)
print(type(number))
