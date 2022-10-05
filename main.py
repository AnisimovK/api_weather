import requests


def user_input_place_id():
    place_id = int(input("Для получения информации о погоде введите:"
                         "\n 0 - Череповец; "
                         "\n 1 - Аэропорт Шереметьево; \n 2 - Лондон;\n"))
    return place_id


def weather_check():
    place = ['Череповец', 'SVO', 'London']
    payload = {'MmnqT': '', 'lang': 'ru'}
    url = f'http://wttr.in/{place[(user_input_place_id())]}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    print(weather_check())


