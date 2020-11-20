import json

# data = json.loads(input())

data = [
    {
        "name": "B",
        "parents": ["A", "C"]
    },
    {
        "name": "C",
        "parents": ["A"]
    },
    {
        "name": "A",
        "parents": []
    },
    {
        "name": "D",
        "parents": ["C", "F"]
    },
    {
        "name": "E",
        "parents": ["D"]
     },
    {
        "name": "F",
        "parents": []
     }
]

parents = {parent['name']: 1 for parent in data}
stack = []
check = set()


for child in data:
    stack.append(child['parents'])
    while stack:
        parent = stack.pop()
        if parent in parents:
            parents[parent] += 1

for i in sorted(parents):
    print(f'{i} : {parents[i]}')
