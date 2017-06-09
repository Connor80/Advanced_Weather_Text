""" Wunderground API """
from WeatherText import *
import requests
import json

atl = "Atlanta"
dal = "Dallas"
tx = "TX"
ga = "GA"
initial_Welcome = "Atlanta or Dallas?"

#For Dallas Weather
dal_link = 'http://api.wunderground.com/api/625080b49667ce19/geolookup/conditions/q/{}/{}.json'.format(tx, dal)
dal_parsed_json = requests.get(dal_link).json()

dal_location = dal_parsed_json['location']['city']
dal_temp_f = dal_parsed_json['current_observation']['temp_f']
dal_weather = dal_parsed_json['current_observation']['weather']
dal_humidity = dal_parsed_json['current_observation']["relative_humidity"]
dal_wind = dal_parsed_json['current_observation']["wind_string"]
dal_rain_1hr = dal_parsed_json['current_observation']["precip_1hr_in"]
dal_rain_day = dal_parsed_json['current_observation']["precip_today_in"]

dal_Welcome = "Hello! It is %s. The current temperature in %s is %s. You can expect %s. Text humidity, wind, rain, sunset, or moon for more information. Text all for all information." % (dal_Date, dal_location, dal_temp_f, dal_weather)
dal_humidityText = "Humidity is at %s." % (dal_humidity)
dal_windText = "The wind is %s." % (dal_wind)
dal_rainText = "%s inches of rain have fallen within the last hour. %s inches total today." % (dal_rain_1hr, dal_rain_day)
dal_allText = "Humidity is at %s. The wind is %s. %s inches of rain have fallen within the last hour. %s inches total today. Sunset is at %s and the moon will be %s." % (dal_humidity, dal_wind, dal_rain_1hr, dal_rain_day, dal_Sunset, dal_Moon)


#For Atlanta Weather
atl_link = 'http://api.wunderground.com/api/625080b49667ce19/geolookup/conditions/q/{}/{}.json'.format(ga, atl)
atl_parsed_json = requests.get(atl_link).json()

atl_location = atl_parsed_json['location']['city']
atl_temp_f = atl_parsed_json['current_observation']['temp_f']
atl_weather = atl_parsed_json['current_observation']['weather']
atl_humidity = atl_parsed_json['current_observation']["relative_humidity"]
atl_wind = atl_parsed_json['current_observation']["wind_string"]
atl_rain_1hr = atl_parsed_json['current_observation']["precip_1hr_in"]
atl_rain_day = atl_parsed_json['current_observation']["precip_today_in"]

atl_Welcome = "Hello! It is %s. The current temperature in %s is %s. You can expect %s. Text humidity, wind, rain, sunset, or moon for more information. Text all for all information." % (atl_Date, atl_location, atl_temp_f, atl_weather)
atl_humidityText = "Humidity is at %s." % (atl_humidity)
atl_windText = "The wind is %s." % (atl_wind)
atl_rainText = "%s inches of rain have fallen within the last hour. %s inches total today." % (atl_rain_1hr, atl_rain_day)
atl_allText = "Humidity is at %s. The wind is %s. %s inches of rain have fallen within the last hour. %s inches total today. Sunset is at %s and the moon will be %s." % (atl_humidity, atl_wind, atl_rain_1hr, atl_rain_day, atl_Sunset, atl_Moon)

#print(dal_Welcome)
#f.close()
