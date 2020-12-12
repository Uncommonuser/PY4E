print("Chapter 8: Exerise 1")

ys = [1, 2, 3, 4, 5, 6]
print(ys)

def chop(ls):
    del ls[0]
    del ls[len(ls)-1]
    print(ls)
    return None

chop(ys)

gs = ['a', 'b', 'c', 'd', 'e','f']

def middle(bs):
    new = list()
    new.extend(bs[1:-1])
    print(new)

middle(ys)
middle(gs)
