import requests


def request_weather():
    payload = {'MmnqT': '', 'lang': 'ru'}
    places = ['Череповец', 'SVO', 'London']
    weather = ''
    for place in places:
        url = f'http://wttr.in/{place}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        weather += response.text
    return weather


if __name__ == '__main__':
    print(weather_request())

