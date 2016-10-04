#8f9d7aa129aca1f28fa3bbc9e950e85d

print("OpenWeatherMap")
import pyowm
owm = pyowm.OWM('8f9d7aa129aca1f28fa3bbc9e950e85d')
observation = owm.weather_at_place('Rostov-on-Don, ru')
weather = observation.get_weather()
location = observation.get_location()

print(owm)
print(observation)
print(weather)
print(location)

print('Страна: '+location.get_country())
print('Город: '+location.get_name())
print('Долгота: '+str(location.get_lon()))
print('Широта: '+str(location.get_lat()))
print('Дождь: '+str(weather.get_rain()))
print('Ветер: '+ str(weather.get_wind()))
print('Статус '+str(weather.get_status()))
