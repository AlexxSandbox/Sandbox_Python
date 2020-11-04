def fibonacci(n):
    """ Вычисление числа Фибоначчи """
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_2(n):
    """ Ряд Фибоначчи """
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib


def main():
    f = open('../Algorithms/input.txt', 'r')
    user_input = int(f.read())
    f.close()
    print(fibonacci(user_input))
    print(fibonacci_2(user_input))


main()
