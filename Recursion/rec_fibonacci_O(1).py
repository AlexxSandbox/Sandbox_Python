def fibonachi(user_input, _cache={}):
    """ Вычисление числа Фибоначчи с памятью"""
    if user_input == 0:
        return _cache.setdefault(user_input, 1)
    elif user_input in _cache:
        return _cache[user_input]
    elif user_input > 2:
        return _cache.setdefault(user_input, fibonachi(user_input - 1) + fibonachi(user_input - 2))
    return user_input


def main():
    f = open('../Algorithms/input.txt', 'r')
    user_input = int(f.read())
    f.close()
    print(fibonachi(user_input))


main()
