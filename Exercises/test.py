text = []
classes = {str(i): [0, 0] for i in range(1, 12)}

with open('dataset_3380_5.txt', 'r') as data:
    for line in data:
        line = line.strip().split('\t')

        if line[0] in classes:
            classes[line[0]][0] += int(line[2])
            classes[line[0]][1] += 1

for key, value in classes.items():
    if value[0] == 0:
        print(key, '-')
    else:
        print(key, value[0] / value[1])
