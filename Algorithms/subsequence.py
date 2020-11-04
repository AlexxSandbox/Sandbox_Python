def str_in_string(string_1, string_2):
    """ Утверждение, что строка string_1 является подстрокой string_2 """
    i = 0
    for j in range(len(string_2)):
        if i < len(string_1) and string_1[i] == string_2[j]:
            i += 1
    if i == len(string_1):
        return 'True'
    return 'False'


def main():
    string_1 = input()
    string_2 = input()
    print(str_in_string(string_1, string_2))


if __name__ == '__main__':
    main()
    # assert str_in_string('abcd', 'hjajlkblkbjkcjld') == 'True'
    # assert str_in_string('cvbn', 'cvb') == 'False'
    # assert str_in_string(' ', '    ') == 'True'
    # assert str_in_string('abc', 'abc') == 'True'
    # assert str_in_string('abc', 'bcd') == 'False'
    # assert str_in_string('abc', ' a b c d ') == 'True'
    # assert str_in_string('abc', 'ahbgdcu') == 'True'
    # assert str_in_string('abcpаdfsdf', 'abcp') == 'False'
