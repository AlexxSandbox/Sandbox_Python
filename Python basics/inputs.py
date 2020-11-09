def text_input():
    with open('input.txt', 'r') as text:
        relatives = {}
        requests = []
        class_count = int(text.readline())
        for _ in range(class_count):
            tmp = text.readline().split()
            relatives[tmp[0]] = [] if len(tmp) == 1 else tmp[2:]

        requests_count = int(text.readline())
        for _ in range(requests_count):
            requests.append(text.readline().split())

    return relatives, requests


def user_input():
    relatives = {}
    requests = []
    for _ in range(int(input())):
        tmp = input().split()
        relatives[tmp[0]] = [] if len(tmp) == 1 else tmp[2:]

    for j in range(int(input())):
        requests.append(input().split())

    return relatives, requests


def is_parents(relatives, request):
    if request[0] == request[1]:
        return 'Yes'

    parents = relatives[request[1]].copy()
    parent = request[0]

    while parents:
        tmp = parents.pop()
        if parent == tmp:
            return 'Yes'

        if relatives[tmp]:
            for i in relatives[tmp]:
                if i not in parents:
                    parents.append(i)

    return 'No'


def main():
    relatives, requests = text_input()
    for request in requests:
        print(is_parents(relatives, request))


main()
