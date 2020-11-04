class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class StackMaxEffective:
    """ Стэк хранит максимум в стэке """
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        if len(self.items) == 1:
            self.max_items.append(item)
            return

        if item > self.max_items[-1]:
            self.max_items.append(item)
        else:
            self.max_items.append(self.max_items[-1])

    def pop(self):
        try:
            self.items.pop()
            self.max_items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        try:
            print(self.max_items[-1])
        except IndexError:
            print('None')


class StackSet:
    """ Стэк из уникальных данных """
    def __init__(self):
        self.items = []
        self.unique_items = set()

    def push(self, item):
        if item not in self.unique_items:
            self.items.append(item)
            self.unique_items.add(item)

    def pop(self):
        try:
            self.unique_items.remove(self.items.pop())
        except IndexError:
            print('error')

    def peek(self):
        try:
            print(self.items[-1])
        except IndexError:
            print('error')

    def size(self):
        print(len(self.items))


# stack = StackMaxEffective()
# commands = []
#
# q = int(input())
# for i in range(q):
#     command = input().split()
#     if command[0] == 'get_max':
#         stack.get_max()
#     elif command[0] == 'pop':
#         stack.pop()
#     elif command[0] == 'push':
#         stack.push(int(command[1]))


# def main():
#     stack = StackSet()
#     commands = []
#     q = int(input())
#     for i in range(q):
#         command = input().split()
#         if command[0] == 'size':
#             stack.size()
#         elif command[0] == 'pop':
#             stack.pop()
#         elif command[0] == 'push':
#             stack.push(command[1])
#         elif command[0] == 'peek':
#             stack.peek()


if __name__ == '__main__':
    main()
