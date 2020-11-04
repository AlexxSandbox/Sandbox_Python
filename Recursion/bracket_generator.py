def bracket_generator(cur, open, close, length):
    """ Генератор скобок
        open - кол-во открытых скобок
        close - кол-во закрытых скобок
        count - длина последовательности
    """
    if len(cur) == 2 * length:
        print(cur)
        return

    if open < length:
        bracket_generator(cur + '(', open + 1, close, length)

    if close < open:
        bracket_generator(cur + ')', open, close + 1, length)


def main():
    length = int(input())
    bracket_generator('', 0, 0, length)


if __name__ == '__main__':
    main()
