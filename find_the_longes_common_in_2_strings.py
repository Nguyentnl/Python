# Given two strings, write a program that efficiently finds the longest common part.

text_1 = raw_input('Enter the first string: ')
# text_1: str
text_2 = raw_input('Enter the second string: ')
# text_2: str


def duplicate(a, b):  # list all the possible common parts in the 2 strings
    list = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i:(i + j + 1)] not in b:
                continue
            else:
                list.append(a[i:(i + j + 1)])
    return list


def longest_string(a, b):  # find the longest common string
    n = duplicate(a, b)
    count = 0
    for m in n:
        if len(m) > count:
            count = len(m)
            word = m
    return "The longest common string is " + word


print longest_string(text_1, text_2)
