class MyQueue:
    """ Класс очереди на основе массива """
    def __init__(self):
        self.items = []

    def __str__(self):
        return self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            print(self.items.pop(0))
        except IndexError:
            print('None')

    def peek(self):
        try:
            print(self.items[0])
        except IndexError:
            print('None')

    def size(self):
        print(len(self.items))

    def is_empty(self):
        print(self.items == 0)


def main():
    stack = MyQueue()
    commands = []
    q = int(input())
    for i in range(q):
        command = input().split()
        if command[0] == 'size':
            stack.size()
        elif command[0] == 'pop':
            stack.pop()
        elif command[0] == 'push':
            stack.push(command[1])
        elif command[0] == 'peek':
            stack.peek()


# def switcher(func, arg=None):
#     stack = MyQueue()
#     switcher = {
#         'size': getattr(stack, 'size')(),
#         'pop': getattr(stack, 'pop')(),
#         # 'push': stack.push(arg),
#         # 'peek': stack.peek()
#     }
#
#     switcher[func]
#
#
# def main():
#     k = int(input())
#     while k > 0:
#         func = input()
#         switcher(func)
#         k -= 1


if __name__ == '__main__':
    main()
