class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value


def print_node(node):
    while node:
        print(node)
        node = node.next


def delete_node(node, index):
    if index == 0:
        head = node.next
        node.next = None
        return head
    else:
        head = node
    while index - 1:
        node = node.next
        index -= 1
    node.next = node.next.next
    return head


def print_reverse(node):
    if node is None:
        return
    head = node
    tail = node.next
    print_reverse(tail)
    print(head)


def print_reverse_2(node):
    while node:
        print(node.value)
        node = node.prev


def reverse_list(node):
    new_head = None
    while node:
        temp = node
        node = temp.next
        temp.next = new_head
        new_head = temp
    return new_head


def find_value(node, value):
    head = node
    index = 0
    while head:
        if value == head.value:
            return index
        else:
            head = head.next
            index += 1
    return -1


def check_loop(node):
    slow_marker = node
    fast_marker = node
    while slow_marker and fast_marker is not None and fast_marker.next is not None:
        slow_marker = slow_marker.next
        fast_marker = fast_marker.next.next
        if slow_marker is fast_marker:
            return True
    return False


node_4 = Node('4')
node_3 = Node('3', node_4)
node_2 = Node('2', node_3)
node_1 = Node('1', node_2)
node_4.next = node_3

# print_node(node_1)
# delete_node(node_1, 2)
#print_node(node_1)
# print_reverse(node_1)
# print(find_value(node_1, '5'))
#reverse_list(node_1)
#print_node(node_4)
# print(check_loop(node_1))
