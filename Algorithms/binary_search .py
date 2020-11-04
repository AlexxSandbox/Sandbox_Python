#  passed 8 окт 2020, 19:59:16 ID:35550607
def bin_search(array, len_array, lost_element):
    """ Бинарный поиск в массиве со смещением сортировки [5, 4, 1, 2, 3]"""
    low = 0
    high = len_array - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == lost_element:
            return mid

        elif array[low] <= array[mid]:
            if array[low] <= lost_element <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1

        elif array[mid] <= lost_element <= array[high]:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def main():
    len_array = int(input())
    lost_element = int(input())
    array = [int(x) for x in input().split()]
    print(bin_search(array, len_array, lost_element))


if __name__ == '__main__':
    main()
