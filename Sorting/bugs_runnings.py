def bugs_runnings(bugs_1, bugs_2):
    """
    Выводим только уникальные номера которые есть в первом и втором
    списках
    """
    bugs_count = {}
    bad_bugs = []
    for bug in bugs_2:
        if bug in bugs_count:
            bugs_count[bug] += 1
        else:
            bugs_count[bug] = 1

    for bug in bugs_1:
        if bug in bugs_count and bug not in bad_bugs:
            bad_bugs.append(bug)
            print(bug, end=' ')


def main():
    len_set_1 = int(input())
    len_set_2 = int(input())
    bugs_1 = [x for x in input().split()] if len_set_1 else []
    bugs_2 = [x for x in input().split()] if len_set_2 else []
    bugs_runnings(bugs_1, bugs_2)


if __name__ == '__main__':
    main()