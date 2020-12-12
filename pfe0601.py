print ("Chapter 6: Exercise 1")

index = None
fruit = 'pineapple'

while True:
    if index is None:
        index = len(fruit)
    elif index >  0:
        letter = fruit[index-1]
        print(letter)
        index = index -1
    else:
        break
