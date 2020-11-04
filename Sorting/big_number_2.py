# passed 17 окт 2020, 22:53:14 ID:36857820
def big_number(numbers):
    sort_numbers = []
    max_len = len(str(max(numbers))) + 1

    for number in numbers:
        tmp = str(number) * max_len
        sort_numbers.append((tmp[:max_len], number))

    sort_numbers.sort(reverse=True)

    for num in sort_numbers:
        print(num[1], end='')


def main():
    numbers_count = int(input())
    numbers = [int(x) for x in input().split()] if numbers_count else []
    big_number(numbers)


if __name__ == '__main__':
    main()
