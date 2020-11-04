class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def solution(node):
    ages = []
    current_level = [node]
    while current_level:
        ages.append([n.value for n in current_level])
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level
    return ages


# root = Node(36, Node(28, Node(32), Node(17)), Node(54, Node(21)))
# s = solution(root)
# print(s)