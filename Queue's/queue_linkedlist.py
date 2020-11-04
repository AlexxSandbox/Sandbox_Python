class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, item):
        if self.tail is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def pop(self):
        if self.head is None:
            return 'error'

        item = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return item

    def peek(self):
        return self.head.value

    def size(self):
        tmp = self.head
        count = 0
        while tmp is not None:
            count += 1
            tmp = tmp.next
        return count

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


def main():
    q = int(input())
    queue = Queue()
    for command in range(q):
        command = input().split()
        if command[0] == 'put':
            queue.put(command[1])
        if command[0] == 'get':
            print(queue.pop())
        if command[0] == 'size':
            print(queue.size())
        if command[0] == 'peek':
            print(queue.peek())


if __name__ == '__main__':
    main()
