# remove the vowel in a string

original = raw_input('Say something: ')

def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t


print anti_vowel(original)

