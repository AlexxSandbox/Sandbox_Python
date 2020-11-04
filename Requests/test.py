import requests

with open('dataset_3378_3.txt', 'r') as source:
    url = source.readline().strip()
    next_file = requests.get(url)
    name = next_file.text
    while True:
        next_url = f'https://stepic.org/media/attachments/course67/3.6.3/{name}'
        file = requests.get(next_url)
        name = file.text
        print(name)
        if file.text.startswith('We'):
            break
