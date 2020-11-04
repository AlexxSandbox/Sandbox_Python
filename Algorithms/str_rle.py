def rle(input_string: str):
    if not input_string:
        return None

    current = input_string[0]
    result = ''

    counter = 1
    for i in range(1, len(input_string)):
        if current == input_string[i]:
            counter += 1
        else:
            result += current + str(counter)
            counter = 1
            current = input_string[i]

    result += current + str(counter)

    return result


if __name__ == '__main__':
    assert rle('AABBCAAA') == 'A2B2C1A3'
    assert rle('AAAAAA') == 'A6'
    assert rle('') is None