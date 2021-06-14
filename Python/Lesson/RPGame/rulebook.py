import sys


class Rule:

    def __init__(self):
        self.__score = 0

    def set_score(self, score):
        self.__score += score
        return self.__score

    def game_over(self):
        print("\nИГРОК ПОВЕРЖЕН!\nGame is over! Your score: "+str(self.__score))
        sys.exit()
