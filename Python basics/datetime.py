from datetime import date, timedelta

y, m, d = map(int, input().split())
days = int(input())
current = date(year=y, month=m, day=d)
current += timedelta(days=days)

print(current.year, current.month, current.day)
