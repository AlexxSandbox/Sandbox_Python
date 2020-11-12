from random import random

# example
lst = [1, 2, 3, 4, 6]
for i in lst:
    print(i)  # 1 2 3 4 6


# example
it = iter(lst)  # class: iterator
while True:
    try:
        i = next(it)  # class method to get next element
        print(i)
    except StopIteration:  # exception when out next element
        break


# example
class RandomIterator:
    """ Creating class iterator """
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return self.i
        else:
            raise StopIteration


for x in RandomIterator(5):
    print(x)  # 1 2 3 4 5


# example
class PrintSecond:
    """ Print every second element """
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration


class MyList(list):
    """ class list with custom iteration method """
    def __iter__(self):
        return PrintSecond(self)


for pair in MyList([1, 2, 3, 4]):
    print(pair)  # (1, 2) (3, 4)


# example
def random_generator(k):
    """ iterator made using generator """
    for i in range(k):
        yield random()


gen = random_generator(3)
for i in gen:
    print(i)
