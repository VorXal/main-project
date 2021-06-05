class Author:

    # Конструктор объекта автор
    def __init__(self, name, email, gender, age):
        self.__name = name
        self.__email = email
        self.__gender = gender
        self.__age = age

    # Получаем имя автора
    def get_name(self):
        return self.__name

    # Получаем e-mail автора (аннотация геттера)
    @property
    def email(self):
        return self.__email

    # Задаем e-mail автора (аннотация сеттера)
    @email.setter
    def email(self, email):
        if len(email) > 10:
            self.__email = email
        else:
            print("Слишком короткий e-mail!")

    # Получаем пол автора
    def get_gender(self):
        return self.__gender

    # Выводим всю информацию об авторе
    def output_info(self):
        print("Автор", self.__name)
        print("Почта", self.__email)
        print("Пол", self.__gender)
        print("Возраст", self.__age)
