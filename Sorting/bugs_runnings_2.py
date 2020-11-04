def bugs_runnings_2(bugs_1, bugs_2):
    """ Вывести номера которые есть в первом и втором списках """
    bugs_count_2 = bugs_count(bugs_2)

    for bug in bugs_1:
        if bug in bugs_count_2 and bugs_count_2[bug] > 0:
            bugs_count_2[bug] -= 1
            print(bug, end=' ')


def bugs_count(bugs):
    dict = {}
    for bug in bugs:
        if bug in dict:
            dict[bug] += 1
        else:
            dict[bug] = 1
    return dict


def main():
    len_set_1 = int(input())
    len_set_2 = int(input())
    bugs_1 = [x for x in input().split()] if len_set_1 else []
    bugs_2 = [x for x in input().split()] if len_set_2 else []
    bugs_runnings_2(bugs_1, bugs_2)


if __name__ == '__main__':
    main()
