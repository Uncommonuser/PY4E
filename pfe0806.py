print ("Chapter 8: Exercise 6")


count = 0
numlist = []

while True:
    ask = input ("Enter a number: ")
    if ask == 'done':
        print('calculating...')
        break
    try:
        value = float(ask)
        numlist.append(value) 
        print ('The number you gave was', value)
        count = count + 1
        print ('The current count is', count)

    except:
        print('Invalid input')



print ('Done! The total of your numbers is', sum(numlist), 'The total numbers you input was', count, 'The max of your data set is', max(numlist), 'While the min of your data set is', min(numlist))
