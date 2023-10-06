import requests

CITY_MAPPINGS = {
    'мск': 'Москва',
    'екб': 'Екатеринбург',
    'питер': 'Санкт-Петербург'
}

API_KEY = '79d1ca96933b0328e1c7e3e7a26cb347'

def get_weather(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&lang=ru&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        wind_speed = round(weather_data['wind']['speed'])

        print('Сейчас в городе', city_name, str(temperature), 'градусов')
        print('Ощущается как', str(temperature_feels), 'градусов')
        print('Скорость ветра', str(wind_speed), 'м/с')
    else:
        print('Ошибка при получении данных о погоде.')

def main():
    print('Для выхода из программы введите "выход".')

    while True:
        city_input = input('Введите город: ').lower()

        if city_input == 'выход':
            break
        elif city_input in CITY_MAPPINGS:
            full_city_name = CITY_MAPPINGS[city_input]
            get_weather(full_city_name)
        else:
            get_weather(city_input)

if __name__ == '__main__':
    main()
