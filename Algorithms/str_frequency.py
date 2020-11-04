def check_frequency(string):
    letters = {}
    result = ''
    for letter in string:
        letters[letter] = letters.get(letter, 0) + 1
    count = sorted(letters.items(), key=lambda x: (-x[1], x[0]))

    for symbol, j in count:
        for _ in range(j):
            result += symbol

    return result


def main():
    string = input()
    print(check_frequency(string))


main()


if __name__ == '__main__':
    print('Test #1 OK' if check_frequency('tree') == 'eert' else 'Test #1 Fail')
    print('Test #2 OK' if check_frequency('ztwidhfk') == 'dfhiktwz' else 'Test #2 Fail')
