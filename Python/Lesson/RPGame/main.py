from rulebook import Rule
from player import Player
from enemy import Enemy
from fight import Fight


if __name__ == "__main__":
    game = Rule()
    gamer = Player("Бальтазар")
    while True:
        monster = Enemy(gamer.get_level())
        print("\nНа арене появляется", monster.get_name(), "!")
        battle = Fight(monster.get_level())
        print(battle.arena(gamer, monster, game))
