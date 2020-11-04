class Node:
    """ Вернуть все левые вершины """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.value)


def solution(node):
    result = []
    current_level = [node]
    while current_level:
        result.append(current_level[0].value)
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level
    return result


# root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(8, Node(17)), Node(10, Node(14))))
# print(solution(root))


