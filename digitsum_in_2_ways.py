#way 1
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
    return total


a = int(raw_input('enter: '))
result = digit_sum(a)
print result

#way 2
a = raw_input('Enter a number: ')
# type: str

total = 0  # type: int
for i in range(len(a)):
  total += int(a[i])
print total
