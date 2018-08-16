# takes in a list and removes elements of the list that are the same


def remove_duplicates(list):
    a = []
    for n in list:
        if n not in a:
            a.append(n)
    return a


print remove_duplicates(["a", "b", "a", "c", "b", "d", "f", "f", "e"])
print remove_duplicates([1, 2, 3, 2, 3, 4, 4, 5, 6, 6, 5, 9, 11, 2])
