import collections


class Conversion:

    def __init__(self, string):
        self.__list = list(string)

    def __str__(self):
        return "Массив: {}".format(self.__list)

    def concatenation(self, string):
        return "".join(self.__list)+string

    def compare_string(self, string):
        if collections.Counter(self.__list) == collections.Counter(string):
            print("Строки ТИПА равны")
        else:
            print("Строки ТИПА не равны")

    def search_symbol(self, symbol):
        return symbol in self.__list

    def list_in_string(self):
        return "".join(self.__list)
