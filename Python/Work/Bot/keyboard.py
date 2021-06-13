from telebot import types


# Создаем клавиатуры
menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
qa_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
close_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

# Создаем кнопки
ticket_button = types.KeyboardButton("Создать заявку")
report_button = types.KeyboardButton("Создать отчет")
qa_button = types.KeyboardButton("Оценить работу отдела")
qa_one_button = types.KeyboardButton("1. Серьезные проблемы")
qa_two_button = types.KeyboardButton("2. Довольно плохо")
qa_three_button = types.KeyboardButton("3. Удовлетворительно")
qa_four_button = types.KeyboardButton("4. Достаточно хорошо")
qa_five_button = types.KeyboardButton("5. Все отлично!")
close_button = types.KeyboardButton("Отмена")

# Привязываем кнопки к клавиатуре
menu_markup.add(ticket_button, report_button)
menu_markup.add(qa_button)
qa_markup.add(qa_five_button)
qa_markup.add(qa_four_button)
qa_markup.add(qa_three_button)
qa_markup.add(qa_two_button)
qa_markup.add(qa_one_button)
close_markup.add(close_button)
