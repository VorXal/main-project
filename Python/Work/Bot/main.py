import telebot
import config
import ticket
import keyboard

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!"
                     .format(message.from_user, bot.get_me()), reply_markup=keyboard.ticket_markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Создать заявку":
        bot.send_message(message.from_user.id, "Введите сообщение, пример:\n\nНе работает VPN"
                                               "\n*Подробное описание проблемы*"
                                               "\n\nДля отмены нажмите - Отмена", reply_markup=keyboard.close_markup)
        bot.register_next_step_handler(message, open_ticket)
    elif message.text == "Создать отчет":
        bot.send_message(message.from_user.id, "Функция пока недоступна")
    else:
        bot.send_message(message.from_user.id, "Команда не распознана")


def open_ticket(message):
    output = ticket.Ticket(message.text)
    bot.send_message(message.from_user.id, output.create_ticket())
    bot.send_message(message.from_user.id, "Чем я еще могу помочь?", reply_markup=keyboard.ticket_markup)


bot.polling(none_stop=True)
