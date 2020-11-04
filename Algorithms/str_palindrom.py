def palindrom_1(phrase):
    """ Провеока, является ли выраженеи палиндромом  """
    phrase = phrase.lower()
    new_phrase = ''
    for letter in phrase:
        if letter.isalpha() or letter.isalnum():
            new_phrase += letter
    reverse_phrase = new_phrase[::-1]
    if reverse_phrase == new_phrase:
        return 'True'
    else:
        return 'False'


def palindrom_2(input_string):
    if not input_string.strip():
        return False
    i = 0
    j = len(input_string) - 1
    while i < j:
        if not input_string[i].isalpha() and not input_string[i].isdigit():
            i += 1
            continue
        if not input_string[j].isalpha() and not input_string[j].isdigit():
            j -= 1
            continue
        if input_string[i].lower() != input_string[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    assert palindrom_2('abba') is True
    assert palindrom_2('abra') is False
    assert palindrom_2('aaaa') is True
    assert palindrom_2('abcba') is True
    assert palindrom_2('AbBa') is True
    assert palindrom_2('abba, cbc abba') is True
    assert palindrom_2('') is False
    assert palindrom_2('        ') is False


# print(palindrom_1(input()))
# print(palindrom_2(input()))