class Book:

    # Конструктор для книг
    def __init__(self, name, price, edition):
        self.__name = name
        self.__author_list = []
        self.__price = price
        self.__edition = edition

    def get_name(self):
        return self.__name

    def append_author(self, author_id, author_list):
        self.__author_list.append(author_list[author_id])

    def remove_author(self, author_id, author_list):
        self.__author_list.remove(author_list[author_id])

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
        print("Автор", self.__author_list)
        print("Цена", self.__price)
        print("Редакция", self.__edition)
