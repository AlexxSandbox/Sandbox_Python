def all_eq(lst):
    if not lst:
        return True

    if len(lst) == 1:
        return True

    v = lst[0]
    for i in range(1, len(lst)):
        if lst[i] != v:
            return False

    return True


def search(winners, coins, target):
    if not coins:
        return all_eq(winners)

    v = coins[-1]

    for i in range(len(winners)):
        if winners[i] + v <= target:
            winners[i] += v
            return search(winners, coins[0:-1], target)

    return False


def main(coins):
    coins.sort()
    s = sum(coins)
    target = s // k

    if s % k == 0 and k <= n and coins[-1] <= target:
        groups = [0] * k
        return search(groups, coins, target)
    else:
        return False


if __name__ == '__main__':
    k = int(input())
    n = int(input())
    coins = [int(x) for x in input().split()]
    print(main(coins))