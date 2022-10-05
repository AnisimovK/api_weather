import requests


def weather_check():
    place_id = int(input("Для получения информации о погоде введите:"
                         "\n 0 - Череповец; "
                         "\n 1 - Аэропорт Шереметьево; \n 2 - Лондон;\n"))
    place = ['Череповец', 'SVO', 'London']
    payload = {'MmnqT': '', 'lang': 'ru'}
    url = f'http://wttr.in/{place[(place_id)]}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    weather_check()


