import re
import sys


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


def search():
    for line in sys.stdin:
        line = line.rstrip()
        line = re.sub(r'((\w)\2)*', r'\2', line)
        print(line)


change_repeat()