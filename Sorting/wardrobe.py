def wardrobe(clothes):
    zero = []
    one = []
    two = []
    for i in clothes:
        if i == '0':
            zero.append(i)
        elif i == '1':
            one.append(i)
        elif i == '2':
            two.append(i)

    array = zero + one + two
    return array


def main():
    count = int(input())
    clothes = [x for x in input().split()] if count else []
    print(' '.join(wardrobe(clothes)))


if __name__ == '__main__':
    main()
