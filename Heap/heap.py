class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def __str__(self):
        return str(self.values)

    def push(self, item):
        self.values.append(item)
        self.size += 1
        self.item_up(self.size - 1)

    def item_up(self, index):
        while index != 0 and self.values[index] < self.values[(index-1)//2]:
            self.values[index], self.values[(index-1)//2] = self.values[(index-1)//2], self.values[index]
            index = (index - 1) // 2

    def item_down(self, index):
        while (2 * index + 1) < self.size:
            j = index
            if self.values[2 * index + 1] < self.values[index]:
                j = 2 * index + 1

            if (2 * index + 2) < self.size and self.values[2 * index + 2] < self.values[j]:
                j = 2 * index + 2

            if index == j:
                break

            self.values[index], self.values[j] = self.values[j], self.values[index]

            index = j

    def get_min(self):
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.item_down(0)
        return tmp


def create_heap(array):
    h = Heap()
    for item in array:
        h.push(item)
    return h


def sort_heap(heap):
    array = []
    while heap.size:
        array.append(heap.get_min())
    return array


a = [2, 4, 1, 7, 3, 8, 9, 0, 10]
heap = create_heap(a)
print(sort_heap(heap))
