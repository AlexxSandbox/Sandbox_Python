import itertools


def fact(x):
    n = 1
    if x > 1:
        for i in range(1, x + 1):
            n = n * i
    return n


def primes():
    n = 1
    while True:
        n += 1
        if (fact(n - 1) + 1) % n == 0:
            yield n


print(list(itertools.takewhile(lambda x: x <= 1000, primes())))
