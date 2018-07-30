# the number of times the item occurs in the list

a = raw_input('Enter a sentence or a list: ')
b = raw_input ('Enter a thing to check: ')


def count(sequence,item):
    count = 0
    for i in sequence:  # type: int
        if i == item:
            count += 1
    return count


print count(a, b)
