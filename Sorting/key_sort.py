def key_sort(array, key):
    sort_array = []
    for k in range(len(key)):
        index = 0
        while index < len(array):
            if array[index] == key[k]:
                sort_array.append(array.pop(index))
                index = 0
            else:
                index += 1

    for i in range(0, len(array) - 1):
        for j in range(i + 1, len(array)):
            if int(array[j]) < int(array[i]):
                array[i], array[j] = array[j], array[i]

    sort_array = sort_array + array
    return sort_array


def main():
    len_array = int(input())
    array = [x for x in input().split()] if len_array else []
    len_key = int(input())
    key = [x for x in input().split()] if len_key else []
    print(' '.join(key_sort(array, key)))


if __name__ == '__main__':
    main()
