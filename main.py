import telebot
from settings import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    username = message.from_user.username
    msg = f'Кто здесь. {username}'
    bot.send_message(message.from_user.id, msg)


bot.polling()
