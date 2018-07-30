# calculate the Fibonacci serie with a given index

# way 1: list and for loop
number = int(raw_input('Enter an index number in Fibonacci: '))
a = [1, 1]


def fibonacci_list(x):
    if x == 0 or x == 1:
        return 1
    elif x == 1:
        return 1
    else:
        for i in range(2, x + 1):
            fib = a[i - 2] + a[i - 1]
            a.append(fib)
        return fib


print fibonacci(number)


# way 2: recursive approach
def fibonacci_recursive(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
