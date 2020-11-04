def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    for number in array:
        print(str(number), end=' ')


def main():
    len_array = int(input())
    array = [int(x) for x in input().split()]
    bubble_sort(array)


if __name__ == '__main__':
    main()
