class Fight:

    def __init__(self, level):
        self.__exp = level * 100
        self.__money = level * 50

    def arena(self, gamer, enemy, game):
        gamer.set_health(enemy.get_power(), game)
        enemy.set_health(gamer.get_power())
        if gamer.get_health() > 0:
            gamer.set_exp(self.__exp)
            gamer.set_money(self.__money)
            game.set_score(self.__money)
            return "\nБой между "+gamer.get_name()+" и "+enemy.get_name()+" окончен!"
