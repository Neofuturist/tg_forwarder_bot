import traceback
import os
from dotenv import load_dotenv
import telebot

load_dotenv()
tgToken = os.environ.get("TELEGRAM_API_TOKEN")
id_from = int(os.environ.get("FROM_USER_ID"))
id_to = int(os.environ.get("TO_USER_ID"))
bot = telebot.TeleBot(tgToken)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print('message')
    try:
        if message.from_user.id == id_from:
            bot.send_message(id_to, str(message.text))
    except Exception as err:
        print('Ошибка:', err)
        print('Описание:\n', traceback.format_exc())


bot.polling(none_stop=True, interval=0)
