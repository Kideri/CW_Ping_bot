import telebot
import config
import ru_en
from telebot import types
from logger.logger import Logger

service = 'GLOBAL'
logger = Logger()
logger.service_init(service)

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    russian = types.KeyboardButton(text='🇷🇺 Русский')
    english = types.KeyboardButton(text='🇺🇸 English')
    keyboard.row(russian, english)
    bot.send_message(message.chat.id, ru_en.welcome, reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)