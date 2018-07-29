# way 1 while
def factorial_while(x):
    factorial = 1
    while x > 1:
        factorial = factorial * x
        x -= 1
    return factorial


print factorial(5)


# way 2 range
def num(x):
    factorial = 1
    if x == 0:
        print("factorial = 1")
    else:
        for i in range(1, x + 1):
            factorial = factorial * i
        return factorial


# way 3: recursion
def factorial_recursive(x):
    if x == 0 or x == 1:
        return 1
    else:
        return factorial(x - 1) * x
