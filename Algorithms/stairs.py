def stairs(steps, steps_count):
    max_steps = 0
    for i in range(steps_count):
        if i <= max_steps:
            max_steps = max(max_steps, i + steps[i])

    print('True' if max_steps >= steps_count else 'False')


def main():
    steps_count = int(input())
    steps = [int(x) for x in input().split()]
    stairs(steps, steps_count)


if __name__ == '__main__':
    main()
