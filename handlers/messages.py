
from telebot import TeleBot


def register_message_handlers(bot: TeleBot):
    @bot.message_handler(func=lambda message: True)  # Обрабатка всех сообщений
    def handle_text(message):
        text = message.text.lower()
        if text == 'hello':
            bot.send_message(
                message.chat.id,
                f'Hello, {message.from_user.first_name} {message.from_user.last_name}'
            )
        elif text == 'id':
            bot.reply_to(message, f'ID: {message.from_user.id}')
        else:
            bot.send_message(message.chat.id, "Извините, я не понимаю эту команду.")
