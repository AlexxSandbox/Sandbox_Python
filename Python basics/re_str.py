import re


def shield():
    """ shielding '\' with row string and with - \ """
    print(r'Hello\world')
    print('Hello\\world')


def re_match():
    """ string start with pattern """
    # [] - show wich elements can be in string
    # [abc] -> a, b, c. aaabc, abc, abbbc
    # [a-d] -> a, b, c, d
    # [a-zA-Z] -> a-z, A-Z
    # [^a-zA-Z] -> all exception a-Z
    patterns = [r'a[abc]+c', r'a\wc']
    user_input = 'accaaaac'
    for pattern in patterns:
        match_object = re.match(pattern, user_input)
        print(match_object)


def re_search():
    """ pattern in anywhere inside string """
    pattern = 'acc'
    user_input = 'baccacc'
    match_object = re.search(pattern, user_input)
    print(match_object.start())


def re_findall():
    """ return all string == pattern """
    # . - any
    # x* - all count x include 0
    # x+ - all count x exclude 0
    # x? - or 0 or 1
    # x{2} - only 2
    # x{2, 4} - 2-4
    patterns = [r'a[abc]c', r'a\wc', r'a\Wc', r'a.c', r'a*c', r'a+c', r'a?c', r'ac{2}']
    user_input = 'abc, acc, aac, dda, a.c'
    for pattern in patterns:
        all = re.findall(pattern, user_input)
        print(all)


def re_sub():
    """ change all patterns to abc """
    pattern = r'a[abc]c'
    user_input = 'abc, acc, aac, dda'
    fix = re.sub(pattern, 'abc', user_input)
    print(fix)


def re_group():
    """ group in re """
    pattern = r'(\w+)-\1'  # \1 - copy (\w+)
    string = ['test-test', 'test-text', 'test-test-test']
    for i in string:
        match = re.match(pattern, i)
        print(match)
