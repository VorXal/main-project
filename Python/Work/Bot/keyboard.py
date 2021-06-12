from telebot import types


# Создаем клавиатуры
ticket_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
close_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

# Создаем кнопки
ticket_button = types.KeyboardButton("Создать заявку")
report_button = types.KeyboardButton("Создать отчет")
close_button = types.KeyboardButton("Отмена")

# Привязываем кнопки к клавиатуре
ticket_markup.add(ticket_button, report_button)
close_markup.add(close_button)
