def mortgage(houses_prices, budget):
    houses_prices.sort()
    count = 0
    for price in houses_prices:
        if price <= budget:
            count += 1
            budget -= price
    print(count)


def main():
    houses, budget = map(int, input().split())
    houses_prices = [int(x) for x in input().split()]
    mortgage(houses_prices, budget)


if __name__ == '__main__':
    main()
