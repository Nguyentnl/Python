# takes in a list of numbers, removes all odd numbers in the list.
def purify(list):
    a=[]
    for n in list:
        if n % 2 == 0:
            a.append(n)
    return a


m = [1, 2, 3, 4, 5, 6]
print purify(m)
