# passed 20 окт 2020, 19:09:13 ID:37269387
def big_number(numbers):
    max_len = len(str(max(numbers)))
    number = sorted(numbers, key=lambda x: (str(x)*max_len)[:max_len], reverse=True)
    return number


def main():
    numbers_count = int(input())
    numbers = [int(x) for x in input().split()] if numbers_count else []
    print(*big_number(numbers), sep='')


if __name__ == '__main__':
    main()
