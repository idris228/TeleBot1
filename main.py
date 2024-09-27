import telebot
from telebot import types

bot = telebot.TeleBot('7046873780:AAGuEnWpwoO32CiF5UQ-oq_bZz854ItC4gQ')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да', callback_data='delete'))
    bot.send_message(message.chat.id, 'Привет! Чашечку утреннго кофе?', reply_markup=markup)


bot.polling(none_stop=True)
