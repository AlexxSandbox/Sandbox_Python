n = 3
a = [[0] * n for i in range(n)]
b = [[0 for j in range(n)] for i in range(n)]
c = [[0] * n] * n  # неправильный вариант - создание трех ссылок на один массив

a[0][0] = 5
c[0][0] = 5
b[0][0] = 5

print(a)
print(b)
print(c)
