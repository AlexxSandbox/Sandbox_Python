from math import ceil

p = 1000000
n = 10
i = 10/(12*100)

# def calc():
#     for k in range(1,n+1):
#         diff_payment = p / n + i * (p - (p * (k - 1)) / n)
#         return (f'Month {k}: paid out {diff_payment:.0f}')
#
# print(calc())

PAYMENT = 8722
INTEREST = 5.6 / (12 * 100)
PERIODS = 120

max_principal = ceil(PAYMENT / ((INTEREST * (1 + INTEREST)**PERIODS) / ((1 + INTEREST)**PERIODS - 1)))
print(max_principal)