class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    # def __repr__(self):
    #     return str(self.value)


def solution(node_1, node_2):

    queue_1 = []
    queue_2 = []

    queue_1.append(node_1)
    queue_2.append(node_2)

    while queue_1 and queue_2:
        node_1 = queue_1[-1]
        node_2 = queue_2[-1]

        if node_1.value != node_2.value:
            return False

        queue_1.pop()
        queue_2.pop()

        if node_1.left and node_2.left:
            queue_1.append(node_1.left)
            queue_2.append(node_2.left)

        elif node_1.left or node_2.left:
            return False

        if node_1.right and node_2.right:
            queue_1.append(node_1.right)
            queue_2.append(node_2.right)

        elif node_1.right or node_2.right:
            return False

    return True


# root_1 = Node(1, Node(1))
# root_2 = Node(1, None, Node(1))
#
# print(solution(root_1, root_2))
