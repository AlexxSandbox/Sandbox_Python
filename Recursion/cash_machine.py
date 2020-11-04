def cash_machine(sum, coins):
    """
    Вывод количества способов которыми можно набрать сумму sum
    coins - номинал монет (списком)
    """
    if sum == 0:
        return 1

    if sum < 0 or not coins:
        return 0

    return cash_machine(sum - coins[0], coins) + cash_machine(sum, coins[1:])


def main():
    sum = int(input())
    count_coins = int(input())
    coins = [int(x) for x in input().split()]
    print(cash_machine(sum, coins))


if __name__ == '__main__':
    main()
