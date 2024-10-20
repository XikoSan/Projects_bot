@bot.message_handler(commands=['remind'])
def remind_command(messag):
    try:
        # Сообщение должно быть в формате: "/remind 2024-10-20 14:30 Напомни..."
        command_parts = messag.text.split('', 3)
        remind_time = datetime.strptime(command_parts[1] + '' + command_parts[2], "%Y-%m-%d %H:%M")
        remind_text = command_parts[3]
        reminders.append({'chat.id': messag.chat.id, 'time': remind_time, 'text': remind_text})
        bot.send_message(messag.chat.id, f'Напоминание установлено на {remind_time}!')
    except (IndexError, ValueError):
        bot.send_message(messag.chat.id, 'Ошибка! Формат должен быть: /remind YYYY-MM-DD HH:MM Текст напоминания')