class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(node):
    result = 0
    current_level = [node]
    while current_level:
        result += 1
        next_level = []
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level
    return result


# root_1 = Node(9, Node(2), Node(7))
# root_2 = Node(3, Node(1, Node(8), Node(12, Node(5))), Node(4))
# print(solution(root_2))
