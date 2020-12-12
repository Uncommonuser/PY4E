print ("Chapter 5: Exercise 1")

sum = 0
count = 0
max = None
min = None

while True:
    ask = input ("Enter a number: ")
    if ask == 'done':
        print('calculating...')
        break
    try:
        ask = float(ask)
        if min is None and max is None:
            min = ask
            max = ask
            print ('The first number is both the max and min', min, max)
        elif ask < min:
            min = ask
            print ('The new min is', min)
        elif ask > max:
            max = ask
            print ('The new max is', max)
        else
            print ("this is not a new max or min")
        print ('The number you gave was', ask)
        count = count + 1
        print ('The current count is', count)
        sum = sum + ask
        print ('The running sum is', sum)

    except:
        print('Invalid input')



print ('Done! The total of your numbers is', sum, 'The total numbers you input was', count, 'The max of your data set is', max, 'While the min of your data set is', min)
