def make_shedule(all_lessons):
    """ Расписание """
    schedule = []
    sort_lessons = sorted(all_lessons, key=lambda x: (float(x[1]), float(x[0])))

    schedule.append(sort_lessons[0])
    for k in range(1, len(sort_lessons)):
        start_lesson = sort_lessons[k][0]
        if float(start_lesson) >= float(schedule[-1][1]):
            schedule.append(sort_lessons[k])

    print(len(schedule))
    for lesson in schedule:
        print(' '.join(lesson))


def main():
    counter_lessons = int(input())
    all_lessons = []
    for i in range(counter_lessons):
        all_lessons.append([lesson for lesson in input().split()])
    make_shedule(all_lessons)


if __name__ == '__main__':
    main()
