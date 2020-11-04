def is_correct_bracket_seq(brackets):
    bracket_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    temp = []
    for bracket in brackets:
        if bracket in bracket_dict:
            temp.append(bracket)
        elif temp and bracket == bracket_dict[temp[-1]]:
            temp.pop()
        else:
            return False
    return len(temp) == 0


if __name__ == '__main__':
    assert is_correct_bracket_seq('') is True
    assert is_correct_bracket_seq('()') is True
    assert is_correct_bracket_seq('[]') is True
    assert is_correct_bracket_seq('({[]})') is True
    assert is_correct_bracket_seq('(]') is False
    assert is_correct_bracket_seq('([])()') is True
