
import telebot
import threading
from config import BOT_TOKEN
from handlers.command import register_command_handlers
from handlers.messages import register_message_handlers
from utils.reminder_checker import check_reminders

bot = telebot.TeleBot(BOT_TOKEN)

# Регистрация обработчиков
register_command_handlers(bot)
register_message_handlers(bot)

if __name__ == '__main__':
    # Запуск потока для проверки напоминаний
    reminder_thread = threading.Thread(target=check_reminders, args=(bot,))
    reminder_thread.start()

    # Запуск бота
    bot.polling(non_stop=True)
