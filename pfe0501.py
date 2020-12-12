print ("Chapter 5: Exercise 1")

count = 0 
sum = 0

while True:
    ask = input ("Enter a number: ")
    try:
        ask = float(ask)
        print ('number', ask)
        count = count + 1
        print ('count', count)
        sum = sum + ask
        print ('sum', sum)
    except:
        print('Invalid input')
    if ask == 'done':
        break
print ('Done! The total of your numbers is', sum, 'The total numbers you input was', count, 'And the average of your numbers is', sum/count)
