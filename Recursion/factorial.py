def rec_factorial(user_input):
    """ Факториал через рекурсию """
    if user_input <= 1:
        return 1
    return rec_factorial(user_input - 1) * user_input


def cycle_factorial(user_input):
    """ Факториал через цикл """
    n = 1
    if user_input > 1:
        for i in range(1, user_input + 1):
            n = n * i
    return n


def main():
    f = open('../Algorithms/input.txt', 'r')
    user_input = int(f.read())
    f.close()
    # print(rec_factorial(user_input))
    print(cycle_factorial(user_input))


if __name__ == '__main__':
    main()
