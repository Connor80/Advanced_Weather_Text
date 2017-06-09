""" Wunderground API """
from WeatherText import Date, Sunset, Moon
import requests
import json


f = 'http://api.wunderground.com/api/625080b49667ce19/geolookup/conditions/q/TX/Dallas.json'
parsed_json = requests.get(f).json()
#json_string = f.read().decode('utf-8')

#parsed_json = json.loads(json_string)

location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
weather = parsed_json['current_observation']['weather']
humidity = parsed_json['current_observation']["relative_humidity"]
wind = parsed_json['current_observation']["wind_string"]
rain_1hr = parsed_json['current_observation']["precip_1hr_in"]
rain_day = parsed_json['current_observation']["precip_today_in"]


Welcome = "Hello! It is %s. The current temperature in %s is %s. You can expect %s. Text humidity, wind, rain, sunset, or moon for more information. Text all for all information." % (Date, location, temp_f, weather)
humidityText = "Humidity is at %s." % (humidity)
windText = "The wind is %s." % (wind)
rainText = "%s inches of rain have fallen within the last hour. %s inches total today." % (rain_1hr, rain_day)
allText = "Humidity is at %s. The wind is %s. %s inches of rain have fallen within the last hour. %s inches total today. Sunset is at %s and the moon will be %s." % (humidity, wind, rain_1hr, rain_day, Sunset, Moon)

print(allText)
#f.close()

""" Future Development
atl = Atlanta
dal = Dallas
tx = TX
ga = GA
atlWeather = 'http://api.wunderground.com/api/625080b49667ce19/geolookup/conditions/q/{}/{}.json'.format(ga, atl)
dalWeather = 'http://api.wunderground.com/api/625080b49667ce19/geolookup/conditions/q/{}/{}.json'.format(tx, dal)
"""
