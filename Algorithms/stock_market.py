def max_income(deals):
    """ Поиск максимальной прибыли на бирже"""
    max_profit = 0
    old_price = deals[0]
    for price in deals:
        if price > old_price:
            max_profit = max_profit + price - old_price
            old_price = price
        elif price < old_price:
            old_price = price
    return max_profit


def main():
    deals_count = int(input())
    deals = [int(x) for x in input().split(' ')] if deals_count else []
    print(max_income(deals))


if __name__ == '__main__':
    main()
