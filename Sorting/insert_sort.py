def inserting_sort(array):
    for i in range(1, len(array)):
        top = i
        while top > 0 and array[top - 1] > array[top]:
            array[top], array[top - 1] = array[top - 1], array[top]
            top -= 1
    for number in array:
        print(str(number), end=' ')


def main():
    len_array = int(input())
    array = [int(x) for x in input().split()]
    inserting_sort(array)


if __name__ == '__main__':
    main()
