import re


class Ticket:

    # Обрезаем сообщение от пользователя
    def __init__(self, message):
        if type(message) != str:
            message = str(message)
        if message == "Отмена":
            self.__theme = "Отмена"
        else:
            self.__theme = re.match('(.*)', message).group(0)
            self.__message = message.replace(self.__theme, "", 1)

    def create_ticket(self):
        error = ""
        alert = False
        if self.__theme == "Отмена":
            return "Создание заявки отменено"
        else:
            if len(self.__theme) < 3:
                error += "Ошибка: Тема сообщения меньше 3 символов\n"
                alert = True
            if len(self.__message) < 12:
                error += "Ошибка: Тело сообщения меньше 12 символов\n"
                alert = True

            if alert == bool(1):
                return error
            else:
                # Отправка письма на почту и возвращение ответа
                return "Заявка создана!"
