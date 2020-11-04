import os
from dotenv import load_dotenv
import json
import requests
from pprint import pprint

load_dotenv()
token = os.getenv('token')
screen_name = os.getenv('my_id')
v = '5.120'
fields = 'sex, about, city, bdate'

params = {'user_ids': screen_name, 'v': v, 'access_token': token, 'fields': fields}
r = requests.get('https://api.vk.com/method/users.get', params=params).json()
f = requests.get('https://api.vk.com/method/friends.get', params=params).json()

result = r.get('response')
pprint(result)

friends= f.get('response').get('items')
pprint(friends)

fields = result[0]
name = fields['first_name']
surname = fields['last_name']
sex_id = fields['sex']

if sex_id == 2:
    sex = 'мужской'
elif sex_id == 1:
    sex = 'женский'
else:
    sex = 'еще не определился'

city_id = fields['city']
city = city_id['title']

print(f'\nПользователь: {name} {surname}, пол {sex}, из города {city}')
