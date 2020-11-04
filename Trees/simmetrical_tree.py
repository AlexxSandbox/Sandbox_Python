class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def anagramma(node_1, node_2):
    if node_1 is None and node_2 is None:
        return True

    if node_1 is not None and node_2 is not None:
        if node_1.value == node_2.value:
            return anagramma(node_1.left, node_2.right) and anagramma(node_1.right, node_2.left)
    return False


def solution(node):
    return anagramma(node, node)
