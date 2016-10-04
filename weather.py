print("OpenWeatherMap")
import pyowm
import datetime
owm = pyowm.OWM('8f9d7aa129aca1f28fa3bbc9e950e85d')

observation = owm.weather_at_place('Rostov-on-Don, ru')
weather = observation.get_weather()
location = observation.get_location()

translatecity ={'Rostov-na-Donu':'Ростов-на-Дону'}
translate ={'RU':'Россия'}
translatestatus ={'Rain':'Не забудьте взять зонт и надувную лодку', 'Clouds':'По нему плывут хмурые тучки'}

def whatiscloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясная'

    if 10 < weather.get_clouds() <= 40:
        return 'облачная'

    if 40< weather.get_clouds()<=100:
        return 'пасмурная'
def whatistemperature():
    if -60 <= weather.get_temperature('celsius')['temp'] <=-30:
        return 'все идет по плану'
    if -30 < weather.get_temperature('celsius')['temp'] <=-20:
        return 'сложно не отморозить нос и уши'
    if -20 < weather.get_temperature('celsius')['temp'] <=0:
        return 'не стоит оставялть шапку дома'
    if 0 < weather.get_temperature('celsius')['temp']<=10:
        return 'необходимы теплые носочки'
    if 10<weather.get_temperature('celsius')['temp']<=20:
        return 'еще можно надеяться на лучшее'
    if 20<weather.get_temperature('celsius')['temp']<=30:
        return 'тепленько'
    if 30< weather.get_temperature('celsius')['temp']<=45:
        return 'попробуйте не изжариться'
def WhatIsWind():
    if 0 <= weather.get_wind()['deg'] < 45:
        return 'северное'

    if 45 <= weather.get_wind()['deg'] < 90:
        return 'северо-восточное'

    if 90 <= weather.get_wind()['deg'] < 135:
        return 'восточное'

    if 135 <= weather.get_wind()['deg'] < 180:
        return 'юго-восточное'

    if 180 <= weather.get_wind()['deg'] < 225:
        return 'южное'

    if 225 <= weather.get_wind()['deg'] < 270:
        return 'юго-западное'

    if 270 <= weather.get_wind()['deg'] < 325:
       return 'западное'

    if 325 <= weather.get_wind()['deg'] <= 360:
        return 'северо-западное '


print('Вас приветствует дружелюбный прогноз погоды! Сегодня, '+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M")+' погода в городе '+translatecity[location.get_name()]+ '('+translate[location.get_country()]+')'+ whatiscloudness()+'. ' + 'Температура '+str(weather.get_temperature('celsius')['temp'])+' градусов Цельсия, '+ whatistemperature()+'. ')
print('Скорость ветра составляет '+str(weather.get_wind()['speed'])+' м/с, '+'направление: '+WhatIsWind()+'. ')
print(translatestatus[str(weather.get_status())]+'. '+'Давление ' +str(weather.get_pressure()['press'])+' мм рт. ст.')