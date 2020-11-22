import requests
import json


def is_interesting(number, info_type='math'):
    url = f'http://numbersapi.com/{number}/{info_type}?json=true'
    res = requests.get(url)
    data = res.json()['found']
    return data


def main():
    with open('numbers.txt', 'r') as f:
        for line in f:
            print('Interesting' if is_interesting(line.rstrip()) else 'Boring')


main()
