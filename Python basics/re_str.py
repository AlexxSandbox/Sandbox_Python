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

def two_cats():
    """ words where two cat or more """
    array = ['catcat', 'cat and cat', 'catac', 'cat', 'ccaatt']
    for line in array:
        if re.findall('cat.*cat', line):
            print(line)


def search_cat():
    """ find words with cat how word """
    array = ['cat', 'catapult and cat', 'catcat', 'concat', 'Cat', '"cat"', '!cat?']
    for line in array:
        if re.search(r'\bcat\b', line):
            print(line)


def z_search():
    """ string where three symbols between z """
    array = ['zabcz', 'zzz', 'zzxzz', 'zz', 'zxz', 'zzxzxxz']
    for line in array:
        if re.search(r'z.{3}z', line):
            print(line)


def slash_search():
    """ find all strings where is slash """
    array = ['\w denotes word character', 'No slashes here']
    for line in array:
        if re.search(r'\\', line):
            print(line)


def tandem_search():
    """ find words where is tandem """
    array = ['blabla is a tandem repetition', '123123 is good too', 'go go', 'aaa']
    for line in array:
        if re.search(r'\b(.+)\1\b', line):
            print(line)


def human_to_computer():
    """ change human to computer """
    array = ['I need to understand the human mind', 'humanity']
    for line in array:
        line = re.sub(r'human', 'computer', line)
        print(line)


def argh():
    """ change first exist aaaa to argh """
    array = ['There’ll be no more "Aaaaaaaaaaaaaaa"', 'AaAaAaA AaAaAaA']
    for line in array:
        line = re.sub(r'\b[a]+\b', 'argh', line, count=1, flags=re.IGNORECASE)
        print(line)


def change_first():
    """ change two first symbol in each string with lenght more than two symbols """
    array = ['this is a text', '"this\' !is. ?n1ce,']
    for line in array:
        line = re.sub(r'\b(\w)(\w)', r'\2\1', line)
        print(line)


def change_repeat():
    """ change all near repeated symbols to one """
    array = ['attraction', 'buzzzz', 'mewmewNnyaaa', 'aaaaaqqqqqqqbbbbb', 'aabb']
    for line in array:
        line = re.sub(r'((\w)\2+)', r'\2', line)
        print(line)
