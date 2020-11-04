def print_alphabet(end_letter, alphabet):
    if alphabet[-1] != end_letter:
        alphabet.pop()
        print_alphabet(end_letter, alphabet)
    return alphabet


def main():
    f = open('../Algorithms/input.txt', 'r')
    end_letter = f.read()
    f.close()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(' '.join(print_alphabet(end_letter, alphabet)))


if __name__ == '__main__':
    main()
