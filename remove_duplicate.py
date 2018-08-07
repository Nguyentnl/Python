# takes in a list and removes elements of the list that are the same


def remove_duplicates(list):
    a = []
    for n in list:
        if n not in a:
            a.append(n)
    return a


print remove_duplicates([1, 2, 1, 3, 2, 4, 5, 3, 2])
