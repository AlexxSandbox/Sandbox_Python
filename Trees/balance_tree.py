class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


def is_balanced(node):
    if node is None:
        return True

    left_height = height(node.left)
    right_height = height(node.right)

    if is_balanced(node.left) is True and is_balanced(node.right) is True:
        if abs(left_height - right_height) <= 1:
            return True
    return False


root_1 = Node(0, Node(2), Node(7, Node(4, Node(12)), Node(8)))
root_2 = Node(1, Node(2), Node(3))


print(is_balanced(root_1))
print(is_balanced(root_2))
print(height(root_1))