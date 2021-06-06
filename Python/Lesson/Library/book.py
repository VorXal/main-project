class Book:

    # Конструктор для книг
    def __init__(self, name, author, price, edition):
        self.__name = name
        if type(author) == list:
            self.__author = author
        else:
            print("Author - не является объектом!")
        self.__price = price
        self.__edition = edition

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_edition(self):
        return self.__edition

    def set_edition(self, edition):
        self.__edition = edition

    def output_info(self):
        print("Книга", self.__name)
        print("Автор", self.__author)
        print("Цена", self.__price)
        print("Редакция", self.__edition)
