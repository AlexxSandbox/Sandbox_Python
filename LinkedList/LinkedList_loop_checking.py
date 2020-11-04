# Floyd's algorithm to check loop in linkedlist
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def hasCycle(node):
    slow_marker = node
    fast_marker = node
    while slow_marker and fast_marker is not None and fast_marker.next is not None:
        slow_marker = slow_marker.next
        fast_marker = fast_marker.next.next
        if slow_marker is fast_marker:
            return True
    return False
