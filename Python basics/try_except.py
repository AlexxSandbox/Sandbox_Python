def f_1(x, y):
    """ return some exception """
    try:
        return x / y
    except (TypeError, ZeroDivisionError):  # isinstance(e, 'exception') == True
        print('Error :(')


print(f_1(5, []))  # Error :(
print(f_1(5, 0))  # Error :(


def f_2(x, y):
    """ return error object - e """
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(e)
        print(type(e))
        print(e.args)


print(f_2(5, 0))
# division by zero
# <class 'ZeroDivisionError'>
# ('division by zero',)


def f_3(x, y):
    """ return any exception """
    try:
        return x / y
    except:  # isinstance any exception with e
        print('Error :(')


print(f_3(5, 0))  # Error :(


def show_mro(error):
    """ Show error's method resolution order"""
    print(error.mro())


show_mro(ZeroDivisionError)  # [<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
show_mro(TypeError) # [<class 'TypeError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]


def f_4(x, y):
    """ try - except - finally """
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero')
    else:  # it will be execute if did not excepts
        print('result is', result)
    finally:  # it will be execute all time
        print('Finally')


f_4(4, 2)  # result is 2.0 + Finally
f_4(4, 0)  # division by zero + Finally
f_4(4, [])  # Finally + 'error'


class NonPositiveError(Exception):
    """ Example user's exception """
    pass


class PositiveList(list):
    """ raise user's exeception if item < 0 """
    def append(self, item):
        if item > 0:
            list.append(self, item)
        else:
            raise NonPositiveError


x = PositiveList()
x.append(-2)  # raise NonPositiveError
