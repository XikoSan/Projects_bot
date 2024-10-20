
import time
from datetime import datetime

# Для хранения напоминаний
reminders = []


#  Регистрация и проверка времени напоминания
def check_reminders(bot):
    while True:
        current_time = datetime.now()
        for reminder in reminders[:]:
            if current_time >= reminder['time']:
                bot.send_message(reminder['chat.id'], f'Напоминание: {reminder["text"]}')
                reminders.remove(reminder)  # Удаляем напоминание после отправки
        time.sleep(60)   # Проверяет каждую минуту
