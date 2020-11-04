def even_sort(array):
    for i in range(len(array) - 1):
        k = i
        if i % 2 == 0 and array[i] % 2 != 0:
            while k < len(array) - 1 and array[k] % 2 != 0:
                k += 1
            while k > i:
                array[k], array[k - 1] = array[k - 1], array[k]
                k -= 1

        elif i % 2 != 0 and array[i] % 2 == 0:
            while k < len(array) - 1 and array[k] % 2 == 0:
                k += 1
            while k > i:
                array[k], array[k - 1] = array[k - 1], array[k]
                k -= 1

    array = [str(x) for x in array]
    return array


def main():
    len_array = int(input())
    array = [int(x) for x in input().split()] if len_array else []
    print(' '.join(even_sort(array)))


if __name__ == '__main__':
    main()
