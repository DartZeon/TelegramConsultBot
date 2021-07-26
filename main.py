import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Понедельник")
    item2 = types.KeyboardButton("Вторник")
    item3 = types.KeyboardButton("Среда")
    item4 = types.KeyboardButton("Четверг")
    item5 = types.KeyboardButton("Пятница")

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def keyboard_message(message):
    if message.chat.type == 'private':
        if message.text == 'Понедельник':
            bot.send_message(message.chat.id, 'Расписание на Понедельник:\n1. Технологии защиты информации (л)\n2. Компьютерные сети\n3. Технологии защиты (пр)')
        elif message.text == 'Вторник':
            bot.send_message(message.chat.id, 'Расписание на Вторник\n1. Организация БД (пр)\n2. Организация БД (л)\n3. Многочисленные методы (л)\n4.Компьютерные сети(пр)\n5.Многочисленные методы (пр)')
        elif message.text == 'Среда':
            bot.send_message(message.chat.id, 'Расписание на Среду\n1. Мигалка: нет пары / Инструментальные средства управления проектами (пр)\n2. Компьютерные сети (пр)\n3. Методы и технологии инженерии по (л)')
        elif message.text == 'Четверг':
            bot.send_message(message.chat.id, 'Расписание на Четверг\n1.Мигалка: Инструментальные средства управления проектами (л) / нет пары\n2.Архитектура компьютеров (л)\n3. Архитектура компьютеров (пр)\n4. Методы и технологии инженерии ПО (пр)')
        elif message.text == 'Пятница':
            bot.send_message(message.chat.id, 'Расписание на Пятницу\n3. Межфакультетская дисциплина')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить :(')

bot.polling()