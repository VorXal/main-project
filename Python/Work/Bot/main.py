import telebot
import config
import ticket


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Обработка событий'
    )
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Work?', callback_data='print'))
    keyboard.add(telebot.types.InlineKeyboardButton('Заявка', callback_data='ticket'))
    bot.send_message(
        message.chat.id,
        'Отправить запрос на сервер',
        reply_markup=keyboard
    )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if type(message.text) == str:
        theme_message = message.text
        text_message = message.text*10
        output = ticket.Ticket(theme_message, text_message)
        bot.send_message(message.from_user.id, output.create_ticket())


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('print'):
        print("Button activated!")
        bot.send_message(query.from_user.id, "WORK!")
    elif data.startswith('ticket'):
        print("New ticket!")
        bot.send_message(query.from_user.id, "Введите тему письма")


bot.polling(none_stop=True)
