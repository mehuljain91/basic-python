import requests
import math

# api key
API_key = ''

# input city name, country name
city = input('Enter a City: ')
country_code = input('Enter Country Code: ')

# openweathermap api
base_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country_code + '&appid=' + API_key

weather_data = requests.get(base_url).json()

# try city name
try: 
    city_name = weather_data['name']
    print("name: " + city_name)
    weather_data.pop('name')
except KeyError:
    print('')

for key, value in weather_data.items():
    if key == 'main':
        main = value
        for k, v in main.items():
            if k == 'temp' or k == 'feels_like' or k == 'temp_min' or k == 'temp_max':
                temp = float(v) - 273.15
                v = str(math.ceil(temp)) + " Celsius"
                print(k, ": ", v)
            if k == 'pressure':
                v = str(v) + 'hPa'
                print(k, ": ", v)
            if k == 'humidity':
                v = str(v) + '%'
                print(k, ": ", v)

    if key == 'visibility':
        vis = value / 1000
        value = str(vis) + 'km'
        print(key, ": ", value)

    else:
        print(key, ": ", value)

    
