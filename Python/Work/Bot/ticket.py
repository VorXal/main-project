class Ticket:

    def __init__(self, theme, message):
        self.__theme = theme
        self.__message = message

    def create_ticket(self):
        return "Тема письма: "+self.__theme+"\n\nТело письма: "+self.__message
