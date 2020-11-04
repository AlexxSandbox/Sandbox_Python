#  passed 6 окт 2020, 20:56:35 ID:35351142
def find_broken_point(array, low_index, high_index):
    if high_index < low_index:
        return -1
    elif high_index == low_index:
        return low_index

    mid_index = (low_index + high_index) // 2
    if mid_index < high_index and array[mid_index] > array[mid_index + 1]:
        return mid_index
    elif mid_index > low_index and array[mid_index] < array[mid_index - 1]:
        return mid_index - 1
    elif array[low_index] >= array[mid_index]:
        return find_broken_point(array, low_index, mid_index - 1)

    return find_broken_point(array, mid_index + 1, high_index)


def bin_search(array, low_index, high_index, lost_element):
    if high_index < low_index:
        return -1

    mid_index = (low_index + high_index) // 2
    if lost_element == array[mid_index]:
        return mid_index
    elif lost_element > array[mid_index]:
        return bin_search(array, mid_index+1, high_index, lost_element)

    return bin_search(array, low_index, mid_index - 1, lost_element)


def search_in_broken_array(array, len_array, lost_element):
    point = find_broken_point(array, 0, len_array - 1)
    if point == -1:
        return bin_search(array, 0, len_array - 1, lost_element)
    elif array[point] == lost_element:
        return point
    elif array[0] <= lost_element:
        return bin_search(array, 0, point - 1, lost_element)

    return bin_search(array, point+1, len_array - 1, lost_element)


def main():
    len_array = int(input())
    lost_element = int(input())
    array = [int(x) for x in input().split()]
    print(search_in_broken_array(array, len_array, lost_element))


if __name__ == '__main__':
    main()
