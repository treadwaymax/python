#! python3
# getOpenWeather.py

import json, requests, sys

APPID = '2abb605433f0461781c4cb54ecd93565'

#compute location from cli arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

#dowloand json data
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

#load json data into python variable
weatherData = json.loads(response.text)

#print weather descriptions
w = weatherData['list']
print(f'current weather in {location}:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('tomorrow')
print(w[1]['weather'][1]['main'], '-', w[1]['weather'][1]['description'])
print()
print('day after tomorrow')
print(w[2]['weather'][2]['main'], '-', w[2]['weather'][2]['description'])
print()

#if __name__ == '__main__':
 #   main()