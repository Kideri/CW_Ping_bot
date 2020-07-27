import telebot
import config
import ru_en
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = types.ReplyKeyboardMarkup()
    russian = types.KeyboardButton(text='\xF0\x9F\x87\xB7\xF0\x9F\x87\xBA Русский')
    english = types.KeyboardButton(text='\xF0\x9F\x87\xBA\xF0\x9F\x87\xB8 English')
    keyboard.add(russian, english)
    bot.send_message(message.chat.id, ru_en.welcome, reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)