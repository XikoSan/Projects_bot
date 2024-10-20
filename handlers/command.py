
from datetime import datetime
from telebot import TeleBot
from utils.web import open_website
from utils.reminder_checker import reminders  # Импорт списка напоминаний
import re


def register_command_handlers(bot: TeleBot):
    # Команда для начала
    @bot.message_handler(commands=['start', 'Hello'])
    def start_command(message):
        bot.send_message(
            message.chat.id,
            f'Hello, {message.from_user.first_name} {message.from_user.last_name}'
        )

    @bot.message_handler(commands=['help'])
    # Команда для помощи
    def help_command(message):
        bot.send_message(
            message.chat.id,
            '<b>Help Information</b>',
            parse_mode='html'
        )

    # Команда для открытия сайта
    @bot.message_handler(commands=['site', 'website'])
    def site_command(message):
        bot.send_message(message.chat.id, "Открываю сайт YouTube...")
        open_website('https://youtube.com')

    @bot.message_handler(commands=['remind'])
    # Команда для установки напоминания
    def remind_command(message):
        try:
            # Получаем текст после команды, например: '/remind 2024-10-20 14:30 Напомни...'
            reminder_text = message.text[len('/remind'):].strip()

            # Регулярное выражение для валидации формата даты и текста
            match = re.match(r'^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) (.+)$', reminder_text)

            if match:
                # Извлекаем дату, время и текст напоминания
                date_str, time_str, remind_text = match.groups()
                remind_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

                # Проверяем, что время напоминания не в прошлом
                if remind_time > datetime.now():
                    # Сохраняем напоминание
                    reminders.append({'chat.id': message.chat.id, 'time': remind_time, 'text': remind_text})
                    bot.send_message(message.chat.id,
                                     f'Напоминание установлено на {remind_time.strftime("%Y-%m-%d %H:%M")}'
                                     f' - {remind_text}')

                else:
                    bot.send_message(message.chat.id,
                                     'Ошибка! Напоминание не может быть установлено на прошедшее время.')
            else:
                bot.send_message(message.chat.id,
                                 'Ошибка! Формат должен быть: /remind YYYY-MM-DD HH:MM Текст напоминания')

        except Exception as e:
            bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')


# Для проверки напоминаний в отдельном потоке
def get_reminders():
    return reminders
