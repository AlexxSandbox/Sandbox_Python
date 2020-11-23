# https://developers.artsy.net/v2/start
import requests
import json


CLIENT_ID = '53833173b4e089cfd490'
CLIENT_SECRET = '84108710914bbc59b914da620990701c'


def get_token(client_id, client_secret):
    token_url = 'https://api.artsy.net/api/tokens/xapp_token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    token_res = requests.post(token_url, data=data)
    client_token = token_res.json()['token']
    return client_token


def get_artist(id, token):
    url = 'https://api.artsy.net/api/artists/'
    headers = {
        'X-XAPP-Token': token
    }
    res = requests.get(url + id, headers=headers)
    artist = res.json()
    return artist


def main():
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    token = get_token(client_id, client_secret)
    artists = []

    with open('artist_id.txt', 'r') as f:
        for line in f:
            artist = get_artist(line.rstrip(), token)
            artists.append([artist['sortable_name'], artist['birthday']])

    artists = sorted(artists, key=lambda x: (int(x[1]), x[0]))
    for artist in artists:
        print(artist[0])


if __name__ == '__main__':
    main()
