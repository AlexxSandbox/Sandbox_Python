def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(a ** 2, n // 2)
    elif n % 2 == 1:
        return pow(a, n - 1) * a


print(pow(4, 2))
print(pow(112, 6))
