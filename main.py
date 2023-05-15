# Франкинштейн для Коли
# Удачи в понимании


import requests
import telebot
import datetime
from telebot import types

#  Ключ для бота, не потеряй
bot = telebot.TeleBot('6236925585:AAGNPQDWA9nwt-3gqc309ptYDzacSiukcJc')


#  Команда для запуска бота
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    #  Это настройки кнопок
    keyboard.row('/help', 'Хочу', 'github', 'дата', 'прогноз', 'version')
    #  Сообщение выводитсья при начале работы с ботом 
    bot.send_message(message.chat.id, ' Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


#  Обьявление кнопки help
@bot.message_handler(commands=['help'])
def start_message(message):
    #  Вывод команды help 
    bot.send_message(message.chat.id, 'github - ссылка на гит \n'
                                      'дата - показать сегодняшнюю дату \n'
                                      'version - показать версию бота \n'
                                      'прогноз - прогноз погоды на неделю \n'
                                      'хочу ли да - ссылка на сайт МТУСИ \n')


#  Обьявление кнопки вызова профиля гит
@bot.message_handler(commands=['github'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ссылка на гитхаб - https://github.com/NikolayBIK21052003')  #  Пока мой, для проверки, не забудь !!!


#  Обьявление кнопки вызова даты
@bot.message_handler(commands=['дата'])
def start_message(message):
    bot.send_message(message.chat.id, str(datetime.date.today()))


#  Обьявление кнопки вызова версии бота
@bot.message_handler(commands=['version'])
def start_message(message):
    bot.send_message(message.chat.id, 'bot version 0.1')


#  Обьявление кнопки вызова прогноза погоды на неделю
@bot.message_handler(commands=['прогноз'])
def start_message(message):
    bot.send_message(message.chat.id, weather_report())


#  Прогноз погоды, не я писал, не мне тут понимать
def weather_report():
    s_city = "Moscow,RU"  # Можно изменить, либо сделать ввод.
    appid = "8f103e9cb5bb949e3cda7be26320a788"  # ключ к openweather
    #  Запрос к openweather, сам прогноз
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    return_data = ''  # Страшные костыли, но по другому никак. Лишь полностью переписывать
    return_data += ("Город: " + s_city + '\n')
    return_data += ("Погодные условия: " + data['weather'][0]['description'] + '\n')
    return_data += ("Температура: " + str(data['main']['temp']) + '\n')
    return_data += ("Минимальная температура: " + str(data['main']['temp_min']) + '\n')
    return_data += ("Максимальная температура " + str(data['main']['temp_max']) + '\n')
    return_data += '\n'
    #  Повторный - хз зачем
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    return_data += ("Прогноз погоды на неделю: " + '\n')
    for i in data['list']: # Писарю, написавшему это - грамота за самый извращенный подход к выводу программы
        return_data += ("Дата < " + i['dt_txt'] + " > \r\nТемпература < " +
              ' {0:+3.0f}'.format(i['main']['temp']) + " > \r\nПогодные условия < " +
              i['weather'][0]['description'] + " > " + '\n')
        return_data += '\n'
    return_data += "____________________________"
    return return_data


#  Проверка на письменные запросы
@bot.message_handler(content_types=['text'])
def answer(message):
    check_message = ('хочу', 'да', 'дата', 'github', 'version', 'прогноз')
    if message.text.lower() == 'хочу':
        bot.send_message(message.chat.id, 'Тогда тебе сюда https://mtuci.ru/')
    elif message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Тогда тебе сюда https://mtuci.ru/')
    elif message.text.lower() == 'дата':
        bot.send_message(message.chat.id, str(datetime.date.today()))
    elif message.text.lower() == 'github':
        bot.send_message(message.chat.id, 'Ссылка на гитхаб - https://github.com/NikolayBIK21052003')
    elif message.text.lower() == 'version':
        bot.send_message(message.chat.id, 'bot version 0.1')
    elif message.text.lower() == 'прогноз':
        bot.send_message(message.chat.id, weather_report())
    if message.text.lower() not in check_message:
        bot.send_message(message.chat.id, 'Команда не распознана! Нажмите Help для справки.')


#  обязательная строка для постоянной работы бота
bot.polling(none_stop=True, interval=0)