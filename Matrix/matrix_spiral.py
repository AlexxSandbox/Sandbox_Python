def spiral_print(row, col, matrix):
    """ Печатаем матрицу по спирали
        k - индекс конечной строки
        l - индекс конечного столбца
        m - кол-во строк
        n - кол-во столбцов
    """
    k = 0
    l = 0
    while k < row and l < col:
        for i in range(l, col):
            print(matrix[k][i])
        k += 1
        for i in range(k, row):
            print(matrix[i][col-1])
        col -= 1
        if k < row:
            for i in range(col-1, l-1, -1):
                print(matrix[row-1][i])
            row -= 1
        if l < col:
            for i in range(row-1, k-1, -1):
                print(matrix[i][l])
            l += 1


def main():
    matrix = []
    row = int(input())
    col = int(input())
    for i in range(row):
        matrix.append(input().split())
    spiral_print(row, col, matrix)


if __name__ == '__main__':
    main()
