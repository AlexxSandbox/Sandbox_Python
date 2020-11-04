a = None
b = 5
c = 3
d = 3

# if a is None and b is not None and c is not None and d is not None:
if a is None and not (b is None or c is None or d is None):
    print("good")
else:
    print('bad')
