def basic_fib(n):
    a, b = 0, 1
    for i in range(n - 1):
        t = a
        a = b
        b += t
    return b
print(basic_fib(100))