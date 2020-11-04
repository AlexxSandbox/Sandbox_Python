def radix_sort(array):
    radix = 10
    max_length = False
    tmp = -1
    placement = 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(radix)]
        for i in array:
            tmp = i // placement
            buckets[tmp % radix].append(i)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1

        placement *= radix
    return ' '.join([str(x) for x in array])


def main():
    numbers_count = int(input())
    numbers = [int(x) for x in input().split()] if numbers_count else []
    print(radix_sort(numbers))


if __name__ == '__main__':
    main()
