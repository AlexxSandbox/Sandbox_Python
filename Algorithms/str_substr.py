def findLongest(s):
    """ Вывести длину самой длинной подстроки которая не повторяется """
    maxlen = 0
    longest = ""
    for i in range(0, len(s)):
        subs = s[i:]
        chars = set()
        for j, c in enumerate(subs):
            if c in chars:
                break
            else:
                chars.add(c)
        else:
            j += 1
        if j > maxlen:
            maxlen = j
            longest = s[i:i + j]
    return longest


def substr(input_string: str):
    """ Вывести длину самой длинной подстроки которая не повторяется """
    i = 0
    j = 0
    current_max = ''
    tmp = ''
    while i < len(input_string):
        if input_string[i] in tmp:
            if not current_max or len(tmp) > len(current_max):
                current_max = tmp
            tmp = ''
            j += 1
            i = j
        tmp += input_string[i]
        i += 1
    return max(len(current_max), len(tmp))


if __name__ == '__main__':
    assert substr('') == 0
    assert substr('aaaaaaa') == 1  # а
    assert substr('abcabc') == 3  # abc
    assert substr('ab') == 2  # ab
    assert substr('abadefaqwerty') == 8  # faqwerty
    assert substr('abcabcacbde') == 5  # abcde


# print(len(findLongest(' '.join(input().split()))))
# print(substr(input()))
