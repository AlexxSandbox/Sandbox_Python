class MyQueueSized:
    def __init__(self, n):
        self.queue = [None for _ in range(n)]
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def __str__(self):
        return self.item

    def put(self, item):
        if self.size != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return None

        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1

        return item

    def queue_size(self):
        return self.size

    def peek(self):
        return self.queue[self.head]


def main():
    q = int(input())
    n = int(input())
    queue = MyQueueSized(n)
    for command in range(q):
        command = input().split()
        if command[0] == 'push':
            queue.put(command[1])
        if command[0] == 'get':
            print(queue.get())
        if command[0] == 'pop':
            print(queue.get())
        if command[0] == 'size':
            print(queue.queue_size())
        if command[0] == 'peek':
            print(queue.peek())


if __name__ == '__main__':
    main()

# q = MyQueueSized(3)
# q.put(1)
# print(q.size)
# q.put(2)
# print(q.queue)
# print(q.get())
# q.put(3)
# print(q.queue)
# q.put(4)
# print(q.queue)
# print(q.get())
