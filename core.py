import telebot
import config
import ru_en

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = types.KeyboardMarkup()
    russian = types.keyboardButton(text='\xF0\x9F\x87\xB7\xF0\x9F\x87\xBA Русский', callback_data='ru_Ru')
    english = types.keyboardButton(test='\xF0\x9F\x87\xBA\xF0\x9F\x87\xB8 English', callback_data='en_US')
    keyboard.add(russian)
    keyboard.add(english)
    bot.send_message(message.chat.id, ru_en.welcome, reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=123)