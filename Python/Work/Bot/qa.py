class quality_control:

    def __init__(self, evaluation, text):
        self.__evaluation = evaluation
        self.__text = text

    def save_eval(self):
        if self.__evaluation == "1. Серьезные проблемы":
            result = "Контакты руководителя: 8-999-999-99-99\nЧто крайне необходимо улучшить?"
        elif self.__evaluation == "2. Довольно плохо":
            result = "Что необходимо улучшить?"
        elif self.__evaluation == "3. Удовлетворительно":
            result = "Что нужно улучшить?"
        elif self.__evaluation == "4. Достаточно хорошо":
            result = "Что можно улучшить?"
        else:
            result = "Спасибо за отзыв!"
        # Запись в базу данных
        return result

    def set_feedback(self, text):
        self.__text = text
        # Запись в базу данных
        return "Спасибо за отзыв!"
