def find_nod(number_1, number_2):
    """ Находим наибольший общий делитель - НОД """
    min_number = min(number_1, number_2)
    max_number = max(number_1, number_2)
    ost = max_number % min_number
    if ost != 0:
        max_number = min_number
        min_number = ost
        return find_nod(max_number, min_number)
    return min_number


def find_nod_2(a, b):
    if b == 0:
        return a
    else:
        return find_nod_2(b, a % b)


def find_nod_3(a, b):
    """ Аогоритм Евклида """
    if a == b:
        return a
    elif a > b:
        return find_nod_3(a - b, b)
    else:
        return find_nod_3(a, b - a)


# def main():
#     f = open('input.txt', 'r')
#     numbers = [int(x) for x in f.read().split()]
#     f.close()
#     print(find_nod(numbers[0], numbers[1]))


# main()
print(find_nod(20, 5))
print(find_nod_2(20, 5))
print(find_nod_3(20, 5))
