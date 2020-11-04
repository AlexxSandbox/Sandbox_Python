def merge(left_array, right_array):
    sorted_list = []
    left_array_index = right_array_index = 0

    left_array_length, right_array_length = len(left_array), len(right_array)

    for _ in range(left_array_length + right_array_length):
        if left_array_index < left_array_length and right_array_index < right_array_length:
            if left_array[left_array_index] <= right_array[right_array_index]:
                sorted_list.append(left_array[left_array_index])
                left_array_index += 1
            else:
                sorted_list.append(right_array[right_array_index])
                right_array_index += 1

        elif left_array_index == left_array_length:
            sorted_list.append(right_array[right_array_index])
            right_array_index += 1

        elif right_array_index == right_array_length:
            sorted_list.append(left_array[left_array_index])
            left_array_index += 1

    return sorted_list


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array, right_array)


def main():
    len_array = int(input())
    array = [int(x) for x in input().split()]
    print(merge_sort(array))


if __name__ == '__main__':
    main()
