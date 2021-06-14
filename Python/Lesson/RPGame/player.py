import random
import rulebook


class Player:

    def __init__(self, name):
        self.__name = name
        self.__level = 1
        self.__exp = 0
        self.__next_up = 1000
        self.__visual = "8"
        self.__max_health = 5 * (10+random.randrange(1, 8))
        self.__max_mana = 5 * (10+random.randrange(1, 8))
        self.__health = self.__max_health
        self.__mana = self.__max_mana
        self.__power = 2 + (5+random.randrange(1, 3))
        self.__magic = 2 + (5+random.randrange(1, 3))
        self.__money = 0

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_power(self):
        return self.__power

    def get_health(self):
        return self.__health

    def set_health(self, damage, game):
        self.__health -= damage
        if self.__health <= 0:
            self.__visual = "X"
            self.__name = "Труп "+self.__name
            print(rulebook.Rule.game_over(game))
        else:
            return self.__health

    def set_money(self, cost):
        self.__money += cost
        return self.__money

    def set_exp(self, exp):
        self.__exp += exp
        print("\nПолучено опыта:", exp)
        if self.__exp >= self.__next_up:
            print("\nУровень повышен!")
            self.__level += 1
            self.__next_up *= 2
            self.__exp = 0
            self.__max_health += self.__level * 50
            self.__max_mana += self.__level * 50
            self.__health = self.__max_health
            self.__mana = self.__max_mana
            print("До следующего уровня:", self.__next_up)
        else:
            print("До следующего уровня:", self.__next_up - self.__exp)

    def get_status(self):
        return "HP: "+str(self.__health)+"/"+str(self.__max_health)+"\nMP: "+str(self.__mana)+"/"+str(self.__max_mana)
