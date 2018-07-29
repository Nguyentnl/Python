# Given two strings, write a program that efficiently finds the longest common subsequence. 
text_1 = raw_input('Enter the first string: ')
# text_1: str
text_2 = raw_input('Enter the second string: ')
# text_2: str

for a, b in zip(text_1, text_2):

    if a == b:
        print a

