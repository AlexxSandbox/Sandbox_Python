# passed on 5 окт 2020, 21:03:58 ID# 35217782
def photo_storage(storages):
    """ Задача про хранилища фотографий """
    photo_count = 0
    storages = sorted(storages, reverse=True)
    while len(storages) > 1 and storages[0] > 0 and storages[1] > 0:
        storages[0] -= 1
        storages[1] -= 1
        photo_count += 1
        storages = sorted(storages, reverse=True)
    return photo_count


def main():
    storage_count = int(input())
    storages = [int(x) for x in input().split()]
    print(photo_storage(storages))


if __name__ == '__main__':
    main()
