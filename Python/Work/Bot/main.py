import telebot
import config
import ticket
import keyboard
import qa

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name} {0.last_name}!"
                                      "\nДля доступа к функциям бота воспользуйтесь предоставленной клавиатурой"
                                      "\nМногие из фич пока что недоступны (по ряду причин)"
                                      "\nAlpha version: 0.1"
                     .format(message.from_user, bot.get_me()), reply_markup=keyboard.menu_markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Создать заявку":
        bot.send_message(message.from_user.id, "Введите сообщение, пример:\n\nНе работает VPN"
                                               "\n*Подробное описание проблемы*"
                                               "\n\nДля отмены нажмите - Отмена", reply_markup=keyboard.close_markup)
        bot.register_next_step_handler(message, open_ticket)
    elif message.text == "Создать отчет":
        bot.send_message(message.from_user.id, "Функция пока недоступна")
    elif message.text == "Оценить работу отдела":
        bot.send_message(message.from_user.id, "*мольба дать фидбэк*", reply_markup=keyboard.qa_markup)
        bot.register_next_step_handler(message, qa_status)
    else:
        bot.send_message(message.from_user.id, "Команда не распознана")


def open_ticket(message):
    ticket_output = ticket.Ticket(message.text)
    bot.send_message(message.from_user.id, ticket_output.create_ticket())
    bot.send_message(message.from_user.id, "Чем я еще могу помочь?", reply_markup=keyboard.menu_markup)


# Блок контроля качества, знаю что кривой (иронично?)
def qa_status(message):
    qa_eval = qa.quality_control(message.text, '')
    bot.send_message(message.from_user.id, qa_eval.save_eval(), reply_markup=keyboard.menu_markup)
    if message.text != "5. Все отлично!":
        bot.register_next_step_handler(message, qa_feedback)


def qa_feedback(message):
    qa_wishes = qa.quality_control('', message.text)
    bot.send_message(message.from_user.id, qa_wishes.set_feedback(message.text))
    bot.send_message(message.from_user.id, "Чем я еще могу помочь?", reply_markup=keyboard.menu_markup)


@bot.message_handler(content_types=['sticker', 'document', 'audio', 'video', 'image'])
def blocking_excess(message):
    bot.send_message(message.from_user.id, "Команда не распознана")


bot.polling(none_stop=True)
