def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def test():
    for i in range(15):
        print("fib[" + str(i) + "]: " + str(fibonacci(i)))

test()
