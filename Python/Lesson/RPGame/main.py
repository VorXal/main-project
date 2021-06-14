from player import Player
from enemy import Enemy


if __name__ == "__main__":
    gamer = Player("Бальтазар", 1, 1000, 1000, 200, 100)
    while True:
        monster = Enemy(gamer.get_level())
        print(monster.get_info())
