MATH_FUNC = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    'mod': lambda a, b: a % b,
    'pow': lambda a, b: a ** b,
    'div': lambda a, b: a // b
}


def calculator(a=None, b=None, func=None):
    if func in MATH_FUNC:
        if func in ('mod', 'div', '/') and b == 0:
            return 'Деление на 0!'
        return MATH_FUNC[func](a, b)
    return 'Не знаю такой операции'


def main():
    a = float(input())
    b = float(input())
    func = input()
    print(calculator(a, b, func))


if __name__ == '__main__':
    main()
