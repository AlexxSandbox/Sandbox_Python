def answer(num):
    s = (int(num) % 100) // 10
    m = (int(num) % 10)
    if s == 1:
        suf = 'программистов'
    elif m == 1:
        suf = 'программист'
    elif m in range(2, 5):
        suf = 'программиста'
    else:
        suf = 'программистов'
    return num, suf


def main():
    num = input()
    print(*answer(num))


if __name__ == '__main__':
    main()
