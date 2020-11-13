import operator as op
from functools import partial

# sort by last surname
x = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

x.sort(key=op.itemgetter(-1))  # get last element in x(i)
print(x)  # [('John', 'Backus'), ('Haskell', 'Curry'), ('Guido', 'van', 'Rossum')]

# some math func
print(op.add(4, 5))  # 9
print(op.pow(4, 2))  # 16
print(op.contains([1, 2, 3], 3))  # 3 in [...] == True

# methodcall - get some method from object
x = ['4a', '1v', '5d', '2b', '3e']
y = x.copy()

# list.sort
f = op.methodcaller('sort')
f(x)
print(x)  # ['1v', '2b', '3e', '4a', '5d']

# list.sort by last element
sort_by_last = partial(list.sort, key=op.itemgetter(-1))
sort_by_last(y)
print(y)  # ['4a', '2b', '5d', '3e', '1v']
