def user_input():
    with open('input.txt', 'r') as text:
        relatives = {}
        requests = []
        class_count = int(text.readline())
        for _ in range(class_count):
            tmp = text.readline().replace(':', '').split()
            if tmp[0] in relatives:
                pass
            else:
                relatives[tmp[0]] = tmp[1:]

        requests_count = int(text.readline())
        for _ in range(requests_count):
            requests.append(text.readline().split())

    return relatives, requests


# print(*user_input(), sep='\n')
# relatives = {'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
# requests = [['A', 'B'], ['B', 'D'], ['C', 'D'], ['D', 'A']]


def check_relatives(relatives, request):
    if request[0] == request[1]:
        return 'Yes'

    parents = relatives[request[1]]
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
    relatives, requests = user_input()
    for request in requests:
        print(check_relatives(relatives, request))


main()
