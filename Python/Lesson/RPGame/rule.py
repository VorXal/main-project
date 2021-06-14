class Rule:

    def __init__(self, score, death):
        self.__score = score
        self.__death = death

    def game_over(self):
        if self.__death is True:
            return "Game is over! Your score:"+self.__score
