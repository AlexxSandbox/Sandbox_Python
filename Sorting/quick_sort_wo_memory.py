def quick_sort(array, start, end):
    if start >= end:
        return array

    i = start
    j = end
    pivot = array[(start + end) // 2]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    quick_sort(array, start, j)
    quick_sort(array, i, end)

    return array


def main():
    len_array = int(input())
    array = [int(x) for x in input().split()]
    sort_array = quick_sort(array, 0, len_array - 1)
    for number in sort_array:
        print(str(number), end=' ')


if __name__ == '__main__':
    main()
