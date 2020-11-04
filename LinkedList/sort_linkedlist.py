class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def sort_list(head):
    if not head:
        return None

    length = 1
    node = head
    tail = None
    while node.next:
        node = node.next
        length += 1
    tail = node
    return merge_sort(head, tail, length)


def merge_sort(head, tail, length):
    if head == tail:
        head.next = None
        return head

    if head.next == tail:
        if head.val < tail.val:
            tail.next = None
            return head
        head.next, tail.next = None, head
        return tail

    i = 1
    node = head
    while i < length / 2:
        node = node.next
        i += 1

    length_1 = length_2 = length / 2
    if length % 2:
        length_2 += 1

    tail_1, head_2 = node, node.next
    left_part = merge_sort(head, tail_1, length_1)
    right_part = merge_sort(head_2, tail, length_2)

    return merge(left_part, right_part)


def merge(head_1, head_2):
    if head_1.val < head_2.val:
        cur, tmp, other = head_1, head_1.next, head_2
    else:
        cur, tmp, other = head_2, head_2.next, head_1
    merged_list = cur

    if not tmp:
        cur.next = other
        return merged_list

    while tmp:
        if tmp.val < other.val:
            cur, tmp = tmp, tmp.next
        else:
            t = tmp
            cur.next = other
            cur = other
            other = t
            tmp = cur.next
        cur.next = other

        return merged_list
