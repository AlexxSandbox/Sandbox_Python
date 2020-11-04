def backpacking(backpack_size, items):
    """ Складываем вещи в рюкзак из массива на входе """
    backpack = []
    backpack_empty = backpack_size
    for item in items:
        if item[2] <= backpack_empty:
            backpack.append(item[0])
            backpack_empty -= int(item[2])
    backpack.sort()
    print(' '.join(str(e) for e in backpack))


def sorting_items(items):
    sort_items = sorted(items, key=lambda x: (-x[1], x[2]))
    return sort_items


def main():
    backpack_size = int(input())
    items_quantity = int(input())
    items = []
    for i in range(items_quantity):
        item = input().split()
        items.append((i, int(item[0]), int(item[1])))
    backpacking(backpack_size,  sorting_items(items))


if __name__ == '__main__':
    main()
