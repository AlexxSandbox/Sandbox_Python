S_FIG = {
    'треугольник': (lambda a, b, c: ((a + b + c) / 2 *
                                     ((a + b + c) / 2 - a) *
                                     ((a + b + c) / 2 - b) *
                                     ((a + b + c) / 2 - c)) ** 0.5, 3),
    'круг': (lambda a: 3.14 * a ** 2, 1),
    'прямоугольник': (lambda a, b: a * b, 2)
}


def square(fig):
    if fig in S_FIG:
        par = []
        for _ in range(S_FIG[fig][1]):
            par.append(int(input()))
        return S_FIG[fig][0](*par)
    return 'Не знаю такую фигуру!'


def main():
    fig = input()
    print(square(fig))


if __name__ == '__main__':
    main()
