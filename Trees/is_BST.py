class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.value)


def in_order(node, path=[]):
    if node.left:
        path = in_order(node.left, path)
    path.append(node.value)
    if node.right:
        path = in_order(node.right, path)
    return path


def solution(node):
    """ Проверка, является ли дерево BST """
    array = in_order(node)
    sort_set = sorted(set(array))
    if array == sort_set:
        return True
    return False


# root = Node(5, Node(3, Node(1), Node(4)), Node(8))
# root_2 = Node(5, Node(3, Node(1), Node(5)), Node(8))
# print(in_order(root))
# print(solution(root_2))
