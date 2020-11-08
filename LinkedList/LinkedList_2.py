class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def clear(self):
        self.__init__()

    def __str__(self):
        if self.head is None:
            return 'LinkedList []'

        cur = self.head
        out = 'LinkedList [' + str(cur.value)
        while cur.next is not None:
            cur = cur.next
            out += ',' + str(cur.value)
        return out + ']'

    def add_head(self, item):
        """ Insert item before head """
        new_node = Node(item)
        self.length += 1
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_tail(self, item):
        """ Insert item after tail """
        new_node = Node(item)
        self.length += 1
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node

    def insert(self, item, index):
        """ Insert item by index """
        new_node = Node(item)
        self.length += 1
        if self.head is None:
            self.head = self.tail = new_node
            return

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        cur = self.head
        cur_index = 0
        while cur is not None:
            cur_index += 1
            if cur_index == index:
                new_node.next = cur.next
                cur.next = new_node
                if cur.next.next is None:
                    self.tail = cur.next
                break
            cur = cur.next

    def remove(self, index):
        """ Remove item by index """
        if self.head is None or index >= self.length:
            return

        self.length -= 1
        if index == 0:
            self.head = self.head.next
            return

        cur = self.head
        cur_index = 0
        while cur is not None:
            cur_index += 1
            if cur_index == index:
                if cur.next.next is None:
                    self.tail = cur
                cur.next = cur.next.next
                break
            cur = cur.next

    def print_items(self):
        """ Print all items """
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

    def check_loop(self):
        """ Check loop in linked list by Floyd algorithms """
        slow_marker = fast_marker = self.head
        while fast_marker is not None and fast_marker.next is not None:
            slow_marker = slow_marker.next
            fast_marker = fast_marker.next.next
            if slow_marker == fast_marker:
                return True
        return False


l = LinkedList()
l.add_head(1)
l.add_tail(2)
l.insert('add', 2)
# l.insert('tail', 2)
print(l)
# l.print_items()
# print(l.check_loop())
l.remove(1)
print(l)