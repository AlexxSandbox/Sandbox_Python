import json

student_1 = {
    'first_name': 'Greg',
    'last_name': 'Dean',
    'scores': [70, 80, 90],
    'description': 'Good job, Greg',
    'certifacate': True
}

student_2 = {
    'first_name': 'Wirt',
    'last_name': 'Wood',
    'scores': [80, 80.2, 80],
    'description': 'Nicely Done',
    'certifacate': True
}

# load to json
data = [student_1, student_2]
print(json.dumps(data, indent=4, sort_keys=True))

# write json
with open('students.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

# load from json
with open('students.json', 'r') as f:
    data_again = json.load(f)
    print(sum(data_again[0]['scores']))
