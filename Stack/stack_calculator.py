# checked on 24 сен 2020, 13:55:43
# ID 34789908
MATH_FUNC = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x
    }


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            return None


def calculator(expression):
    stack = Stack()
    math_func = MATH_FUNC

    for symbol in expression:
        if symbol in math_func:
            x = stack.pop()
            y = stack.pop()
            result = math_func[symbol](x, y)
            stack.push(result)
        else:
            stack.push(int(symbol))
    return stack.pop()


def main():
    expr = input()
    print(calculator(expr.split()))


if __name__ == '__main__':
    main()
