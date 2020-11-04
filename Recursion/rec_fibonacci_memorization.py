def fibonachi(user_input, f_numbers={0:1, 1:1}):
    """ Вычисление числа Фибоначчи с памятью"""
    if user_input not in f_numbers:
        f_numbers[user_input] = fibonachi(user_input-1, f_numbers) + fibonachi(user_input-2, f_numbers)
    return f_numbers[user_input]


def main():
    f = open('../Algorithms/input.txt', 'r')
    user_input = int(f.read())
    f.close()
    print(fibonachi(user_input))


main()
