import requests


def weather_check():
    place_id = input("Для получения информации о погоде введите:"
                         "\n 0 - Череповец; "
                         "\n 1 - Аэропорт Шереметьево; \n 'Элтон Джон - мой герой' - Лондон;\n")
    if place_id == 'Элтон Джон - мой герой':
        place_id = 2
    place = ['Череповец', 'SVO', 'London']
    url = f'http://wttr.in/{place[int(place_id)]}?MmnqT&lang=ru'
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    weather_check()


