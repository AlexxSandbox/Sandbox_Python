def len_last_word(string):
    print(len(string[-1]))


def main():
    string = [x for x in input().split()]
    len_last_word(string)


if __name__ == '__main__':
    main()
