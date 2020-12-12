print ("Chapter 6: Exercise 3")


fruit = 'pineapple'

def count (x, y):
    counter = 0
    for letter in x:
        if letter == y:
            counter = counter + 1
    print(counter)

count(fruit, 'a')
