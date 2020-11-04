class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


def find_max(node):
    if node is None:
        return float('-inf')

    max = node.value

    left_max = find_max(node.left)
    right_max = find_max(node.right)

    if left_max > max:
        max = left_max

    if right_max > max:
        max = right_max

    return max


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    print(find_max(root))