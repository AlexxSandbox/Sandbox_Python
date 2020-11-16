def substr(s, t):
    k = 0
    while t in s:
        k += 1
        i = s.find(t) + 1
        s = s[i:]
    return k


def main():
    s, t = [input() for x in range(2)]
    print(substr(s, t))


assert substr('abababa', 'aba') == 3
assert substr('abababa', 'abc') == 0
assert substr('aaaaa', 'a') == 5
assert substr('abc', 'abc') == 1