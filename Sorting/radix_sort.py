# passed 20 окт 2020, 18:57:17 ID:37265901
def radix_sort(numbers):
    length = len(str(max(numbers)))
    rang = 10

    for i in range(length):
        tmp_array = [[] for _ in range(rang)]
        divider = 10**i

        for num in numbers:
            num_rang = num // divider % 10
            tmp_array[num_rang].append(num)

        numbers = []
        for k in range(rang):
            numbers += tmp_array[k]

    return numbers


def main():
    num_count = int(input())
    numbers = [int(x) for x in input().split()] if num_count else []
    print(*radix_sort(numbers), sep=' ')


if __name__ == '__main__':
    main()
