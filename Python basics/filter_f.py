""" filter - iterator, return items, which corresponding filter's func """
print(filter.__doc__)


# example
def even(x):
    return x % 2 == 0


array = [10, 11, 14, 15, 21, 26]
iter_even = filter(even, array)
list_even = list(filter(even, array))
print(*iter_even)  # 10 14 26
print(*list_even)  # 10 14 26


# example
