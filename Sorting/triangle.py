def triangle(array):
    sides = sorted(array, reverse=True)
    for i in range(2, len(array) - 1):
        while sides[i - 2] >= sides[i - 1] + sides[i]:
            i += 1
        break
    p = sides[i - 2] + sides[i - 1] + sides[i]
    return p


def main():
    len_array = int(input())
    sides = [int(x) for x in input().split()]
    print(triangle(sides))


if __name__ == '__main__':
    main()
