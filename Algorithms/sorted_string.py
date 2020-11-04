def sorting_string(strings, string_count, string_length):
    count_to_delete = 0
    for x in range(string_length):
        for y in range(string_count - 1):
            if strings[y][x] > strings[y+1][x]:
                count_to_delete += 1
                break
    return count_to_delete


def main():
    strings = []
    string_count = int(input())
    string_length = int(input())
    for _ in range(string_count):
        strings.append(input())
    print(sorting_string(strings, string_count, string_length))


if __name__ == '__main__':
    main()
