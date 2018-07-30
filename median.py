# calculate the median of a list of numbers

n = [3, 5, 7]
m = [5, 12, 13, 11, 4, 6, 1, 8, 9, 0]


def median(x):
    x.sort()
    if len(x) % 2 == 1:
        median = x[int(len(x) / 2)]
    else:
        total = x[len(x) / 2] + x[len(x) / 2 - 1]
        median = float(total) / 2

    return median


print median(n)
print median(m)
