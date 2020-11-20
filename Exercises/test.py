import json


def check_parents(data):
    counter = {item['name']: 1 for item in data}
    relatives = {item['name']: item['parents'] for item in data}
    stack = []

    for child in relatives:
        check = set()
        stack += relatives[child]
        while stack:
            parent = stack.pop()
            if parent not in check:
                counter[parent] += 1
            stack += relatives[parent]
            check.add(parent)

    return counter


def main():
    data = json.loads(input())
    parents = check_parents(data)
    for parent in sorted(parents):
        print(f'{parent} : {parents[parent]}')


if __name__ == '__main__':
    main()
