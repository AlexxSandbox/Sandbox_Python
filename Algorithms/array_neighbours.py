""" Вывести соседние элементы в матрице """


# n = int(input())
# m = int(input())
# matrix = [input().split() for _ in range(n)]
# i, j = int(input()), int(input())
# neighbors = []
# col_size = len(matrix)
# row_size = len(matrix[0])
#
# if i != 0:
#     neighbors.append(matrix[i-1][j])
# if i != col_size - 1:
#     neighbors.append(matrix[i+1][j])
# if j != 0:
#     neighbors.append(matrix[i][j-1])
# if j != row_size - 1:
#     neighbors.append(matrix[i][j+1])
#
# neighbors = [int(x) for x in neighbors]
# neighbors.sort()
#
# print(' '.join([str(x) for x in neighbors]))


class People:
    def __init__(self, people):
        self.people = people

    def get_neigbours(self, x, y):
        result = []

        if x > 0:
            result.append(self.people[x - 1][y])
        if y > 0:
            result.append(self.people[x][y - 1])
        if y < len(self.people[x]) - 1:
            result.append(self.people[x][y + 1])
        if x < len(self.people) - 1:
            result.append(self.people[x + 1][y])

        return sorted(result)


if __name__ == '__main__':
    people = People([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    assert people.get_neigbours(1, 1) == [2, 4, 6, 8]
    assert people.get_neigbours(0, 0) == [2, 4]
    assert people.get_neigbours(2, 2) == [6, 8]
