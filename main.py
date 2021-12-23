import telebot
from telebot import types
token ='5091745801:AAEK2HzD_vwB6CQDrOMHlTCWNSgr1_kiH-s'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Этот бот может отвечать на сообщения. Для этого отправьте любую из следующих команд: ')

@bot.message_handler(commands=['z1'])
def first_m(message):
    bot.send_message(message.chat.id, 'Я родился')

@bot.message_handler(commands=['z2'])
def second_m(message):
    bot.send_message(message.chat.id, 'Я вырос')


@bot.message_handler(commands=['z3'])
def blin_m(message):
    bot.send_message(message.chat.id, 'Я умер')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "мудси":
        bot.send_message(message.chat.id, '''ЛУЧШИЙ УНИВЕР В МИРЕ''')
    if message.text.lower() == "линукс":
        bot.send_message(message.chat.id, 'ЛУЧШАЯ ОС В МИРЕ')
    if message.text.lower() == "эпл":
        bot.send_message(message.chat.id, 'ЛУЧШАЯ ТЕХНИКА В МИРЕ')
    if message.text.lower() == "андроид":
        bot.send_message(message.chat.id, 'ПЛОХО')
    else:
        bot.send_message(message.chat.id, 'Чета плохо стелишь братанчик')



bot.infinity_polling()
