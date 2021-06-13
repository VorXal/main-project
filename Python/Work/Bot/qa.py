class quality_control:

    def __init__(self, evaluation):
        self.__evaluation = evaluation

    def save_eval(self):
        # Запись в базу данных

        if self.__evaluation == "1. Серьезные проблемы":
            return "Просьба связаться с руководителем.\nКонтакты: 8-999-999-99-99"
        else:
            return "Благодарим за отзыв, ваша оценка: "+self.__evaluation
