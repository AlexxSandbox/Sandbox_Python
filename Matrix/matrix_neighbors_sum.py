matrix = []

while True:
    user_input = input()
    if user_input == 'end':
        break
    else:
        matrix.append([int(x) for x in user_input.split()])

new_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

m = len(matrix[0])
n = len(matrix)

for i in range(n):
    for j in range(m):
        right = matrix[i][(j + 1) % m]
        down = matrix[(i + 1) % n][j]
        letf = matrix[i][j - 1]
        up = matrix[i - 1][j]
        new_matrix[i][j] = right + down + letf + up

for array in new_matrix:
    print(*array)
