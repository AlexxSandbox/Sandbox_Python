import math


class Stack:
    def __init__(self):
        self.items = []

    def __bool__(self):
        return bool(self.items)

    def push(self, item):
        if self.items:
            self.items.append((item, min(item, self.items[-1][1])))
        else:
            self.items.append((item, item))

    def pop(self):
        try:
            return self.items.pop()[0]
        except IndexError:
            return None

    def get_min(self):
        if not self.items:
            return math.inf
        return self.items[-1][1]

    def is_empty(self):
        return self.items == []


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, item):
        self.s1.push(item)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def get_min(self):
        return min(self.s1.get_min(), self.s2.get_min())

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()


def photo_storage(storages):
    """ Решение задачи про хранилища для фотографий через очередь на двух стеках """
    count = 0
    data_centres = Queue()
    for storage in storages:
        data_centres.push(storage)
    min = data_centres.get_min()
    current_storage = data_centres.pop()
    count += 1
    copies = count * min
    tmp = current_storage - min
    storages.append(tmp)
    photo_storage(storages)
    return copies // 2


def main():
    storage_count = int(input())
    storages = [int(x) for x in input().split()]
    print(photo_storage(storages))


if __name__ == '__main__':
    main()
