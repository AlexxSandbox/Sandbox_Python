def q(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return q(n-1, k) + q(n-1, k-1)


n, k = map(int, input().split())
print(q(n, k))
