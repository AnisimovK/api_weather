import requests


def weather_request(place):

    payload = {'MmnqT': '', 'lang': 'ru'}
    url = f'http://wttr.in/{place}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def weather_print():
    places = ['Череповец', 'SVO', 'London']
    for place in places:
        print(weather_request(place))


if __name__ == '__main__':
    weather_print()
