def flower_coordinate(flowers):
    if len(flowers) <= 1:
        return flowers

    coord = []
    flowers = sorted(flowers, key=lambda x: (x[0], x[1]))
    coord.append(flowers[0])
    for k in range(1, len(flowers)):
        if coord[-1][0] == flowers[k][0]:
            if coord[-1][1] < flowers[k][1]:
                coord[-1][1] = flowers[k][1]

        elif coord[-1][0] < flowers[k][0] <= coord[-1][1]:
            if coord[-1][1] <= flowers[k][1]:
                coord[-1][1] = flowers[k][1]

        else:
            coord.append(flowers[k])

    for x,y in coord:
        print(str(x),str(y))


def main():
    flowers_coord = []
    gardener_count = int(input())
    if gardener_count:
        for _ in range(gardener_count):
            flowers_coord.append([int(x) for x in input().split()])
    flower_coordinate(flowers_coord)


if __name__ == '__main__':
    main()
