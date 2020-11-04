from datetime import datetime


def timer(func):
    """ Декоратор для замера скорости выполенния программ """
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print('time spend:', datetime.now() - start)
        return result
    return wrapper


@timer
def hungry_kids_slow(kids, cookies):
    """ Медленный поиск из-за вложенного цикла for """
    count = 0
    for kid in kids:
        for cookie in sorted(cookies):
            if kid <= cookie:
                cookies.remove(cookie)
                count += 1
                break
    return count


@timer
def hungry_kids_fast(kids, cookies):
    """ Быстрый поиск """
    count = 0
    cookies = sorted(cookies)
    for kid in sorted(kids, reverse=True):
        if len(cookies) > 0:
            if cookies[-1] >= kid:
                count += 1
                cookies.pop()
        else:
            break
    return count


def main():
    """ kids_count - кол-во детей
        kids - дети с уровнем жадности (числа через пробел)
        cookie_count - кол-во печенек
        cookies - печеньки (числа в строку)
    """
    kids_count = int(input())
    kids = [int(x) for x in input().split()] if kids_count else []
    cookie_count = int(input())
    cookies = [int(x) for x in input().split()] if cookie_count else []
    print(hungry_kids_fast(kids, cookies))
    print(hungry_kids_slow(kids, cookies))


if __name__ == '__main__':
    main()
    # print('Test #1 OK' if (hungry_kids_slow([1, 2], [1, 2, 3]) == 2) else 'Test #1 Fail')
    # print('Test #2 OK' if (hungry_kids_slow([1, 2, 3], [1, 1]) == 1) else 'Test #2 Fail')
    # print('Test #3 OK' if (hungry_kids_slow([3], [1, 1]) == 0) else 'Test #3 Fail')
    # print('Test #4 OK' if (hungry_kids_slow([1, 2, 3], [1, ]) == 1) else 'Test #4 Fail')
    # print('Test #5 OK' if (hungry_kids_slow([1], []) == 0) else 'Test #5 Fail')
    # print('Test #6 OK' if (hungry_kids_slow([1, 2, 3], [1]) == 1) else 'Test #6 Fail')
    # print('Test #7 OK' if (hungry_kids_slow([3, 3, 2, 3], [1, 2, 1, 2, 1]) == 1) else 'Test #7 Fail')
    #
    # print('Test #1 OK' if (hungry_kids_fast([1, 2], [1, 2, 3]) == 2) else 'Test #1 Fail')
    # print('Test #2 OK' if (hungry_kids_fast([1, 2, 3], [1, 1]) == 1) else 'Test #2 Fail')
    # print('Test #3 OK' if (hungry_kids_fast([3], [1, 1]) == 0) else 'Test #3 Fail')
    # print('Test #4 OK' if (hungry_kids_fast([1, 2, 3], [1, ]) == 1) else 'Test #4 Fail')
    # print('Test #5 OK' if (hungry_kids_fast([1], []) == 0) else 'Test #5 Fail')
    # print('Test #6 OK' if (hungry_kids_fast([1, 2, 3], [1]) == 1) else 'Test #6 Fail')
    # print('Test #7 OK' if (hungry_kids_fast([3, 3, 2, 3], [1, 2, 1, 2, 1]) == 1) else 'Test #7 Fail')
