def some_print(a, b):
    """ Вывод аргументов функции """
    print(a, b)


some_print(10, 20)  # позиционный
some_print(a=10, b=20)  # именованный
some_print(10, b=20)  # позиционные всегда в первую очередь

# Перебор объектов для фукнции из списка в качестве позиционных аргументов
lst = [30, 40]
some_print(*lst)

# Перебор именованных объектов из словаря в качестве именованных аргументов
numbers = {'a': 50, 'b': 60}
some_print(**numbers)


def args_print(a, b, *args):
    """ Вывод аргументов функции + доп/неициализированных позиционных """
    print(a, b, sep=' ', end=' ')
    for arg in args:
        print(arg, end=' ')


# все аргументы, кроме a и b попадают в кортеж (30, 40, 50)
args_print(10, 20, 30, 40, 50)


def kwargs_print(a, b, **kwargs):
    """ Вывод аргументов функции + доп/неициализированных именованных """
    print(a, b, sep=' ', end=' ')
    for key in kwargs:
        print(kwargs[key], sep=' ', end=' ')


# все аргументы, кроме a и b попадают в словарь {'c':30, 'd':40, 'test':50}
print()
kwargs_print(10, c=30, d=40, test=50, b=20)


# далее какая то магия
a = 1
b = 2
lst = [5, 6, 7, 8]
dct = {"1": 11, "2": 22}
print(a, b, lst, dct)


def pr(aa, bb, cc, *llst, **ddct):
    """ Вывод аргументов, пока не постижимый сознанию """
    print(aa)  # 1
    print(bb)  # 2
    print(cc)  # возьмётся из списка - 5
    print(llst)  # остатки списка в виде кортежа - (6, 7, 8)
    print(lst)  # глобальная переменная - [5, 6, 7, 8]
    for k in ddct:
        print(k, ddct[k])
    print(ddct)  # словарь в к-й попали dct, r=8,t=6
    print(*llst)  # элементы кортежа - 6 7 8
    print(*ddct)  # ключи словаря - 1 2 r t
    print(*dct)  # глобальная переменная - 1 2


pr(a, b, *lst, **dct, r=8, t=6)
