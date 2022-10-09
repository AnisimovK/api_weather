import requests


def request_text(url, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    payload = {'MnqT': '', 'lang': 'ru'}
    places = ['Череповец', 'SVO', 'London']
    for place in places:
        url = f'http://wttr.in/{place}'
        print(request_text(url, payload))