# -*- coding: utf-8 -*-
import pyowm
import telebot
import datetime
from datetime import datetime
from telebot import types
import urllib
from xml.etree import ElementTree as ET
import urllib.request

bot = telebot.TeleBot('933240067:AAFBmSPmdMwmWTrE6gcMXljc1UZhZWZxfvQ');

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_chat_action(chat_id=chat_id, action='typing')
    bot.send_message(chat_id, 'Приветствую! Я кроки-бот, способный сориентировать Вас в мире переменчивой погоды и нестабильных цифр в финансовом мире. Для продолжения работы, пожалуйста, введите команду “/menu”')
    
@bot.message_handler(commands=['menu']) 
def main_f(message):
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('Курс валют',callback_data='Курс валют')  
    )  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('Погода',callback_data='Погода'),  
    )
    bot.send_message(message.chat.id,'Выберите нужную функцию:',reply_markup=keyboard)
    bot.send_message(message.chat.id,text =("Это сообщение скоро пропадет"))


@bot.callback_query_handler(func=lambda c:True)
def inline(c):
  z = c.message.message_id+1
  if c.data == 'Погода':
    rpl = temp()
    bot.edit_message_text(chat_id=c.message.chat.id, message_id=z, text=rpl)
  if c.data == 'Курс валют':
    rpl = dollar_evro()
    bot.edit_message_text(chat_id=c.message.chat.id, message_id=z, text=rpl)
    

def temp():
    api = pyowm.OWM('6880b20ccde2b29f7f3bac0160a31959') 
    data = api.weather_at_place("Санкт-Петербург" + ",ru")
    weather = data.get_weather()     
    temperature = weather.get_temperature('celsius')
    clouds = weather.get_clouds()
    t = str(temperature.get('temp')) + '°C'
    wind = weather.get_wind()

    if 0 <= clouds <= 5:
        str_weather = 'Сейчас в Санкт-Петербурге' + t + '\nВетер' + str(wind.get('speed')) + 'm/s\n'+' Безоблачно '
    else:
        str_weather = 'Сейчас в Санкт-Петербурге ' + t  + '\nВетер ' + str(wind.get('speed')) + 'm/s' +'\nОблачно '
    return str_weather


 
def dollar_evro():
 
    id_dollar = "R01235"
    id_evro = "R01239"
    date = datetime.today().strftime('%d/%m/%Y')
    valuta = ET.parse(urllib.request.urlopen(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"))
 
    for  line in valuta.findall('Valute'):
        id_v = line.get('ID')
        if id_v == id_dollar:
            rub_dollar = line.find('Value').text
        if id_v == id_evro:
            rub_evro = line.find('Value').text
    res = 'RUB - USD ' +str(rub_dollar) + "\n" + 'RUB - EUR ' + str(rub_evro) + "\n" + "Данные актуальны на: " + str(date)
    return res

bot.polling(none_stop=True, interval=0)
