def decoder(code, keys):
    pass


def main():
    code = input()
    key_count = int(input())
    keys = []
    for _ in range(key_count):
        keys.append(input())
    decoder(code, keys)


if __name__ == '__main__':
    main()
