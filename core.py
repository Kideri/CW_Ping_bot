import telebot
import config
import ru_en
from telebot import types
from logger.logger import Logger
from database.db_controller import Controller
from comands.parser import Parser
from comands.worker import Worker

service = 'GLOBAL'
logger = Logger()
logger.service_init(service)
controller = Controller(logger)
worker = Worker(logger, controller)
parser = Parser(logger, worker)


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_command(message):
    controller.create_user(message.chat.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    russian = types.KeyboardButton(text='🇷🇺 Русский')
    english = types.KeyboardButton(text='🇺🇸 English')
    keyboard.row(russian, english)
    bot.send_message(message.chat.id, ru_en.welcome, reply_markup=keyboard)


@bot.message_handler()
def text(message):
    reply = parser.parse(message.chat.id, message.text)
    if reply == 'failed':
        return
    bot.send_message(message.chat.id, reply)


if __name__ == '__main__':
    bot.polling(none_stop=True)