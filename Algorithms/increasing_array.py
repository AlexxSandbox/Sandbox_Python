def increasing_array(array):
    increase = 1
    result = []
    for i in range(len(array) - 1):
        if array[i] < array[i+1]:
            increase += 1
        elif array[i] > array[i+1]:
            result.append(increase)
            increase = 1
    result.append(increase)
    print(max(result))


def main():
    count_nums = int(input())
    array = [int(x) for x in input().split()] if count_nums > 0 else []
    increasing_array(array)


if __name__ == '__main__':
    main()
