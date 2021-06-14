import random


class Enemy:

    def __init__(self, hero_level):
        level = random.randrange(hero_level, hero_level+2)
        self.__monsters = ["Демон", "Гоблин", "Скелет", "Суккуб", "Вервольф"]
        self.__grade_monsters = ["Младший ", "Старший ", "Архи-"]
        rand_m = random.randrange(0, len(self.__monsters))
        rand_g = random.randrange(0, len(self.__grade_monsters))
        if rand_g == 1:
            level += 1
        elif rand_g == 2:
            level += 2
        self.__name = self.__grade_monsters[rand_g] + self.__monsters[rand_m]
        self.__health = level * random.randrange(50, 100)
        self.__power = level + random.randrange(1, 10)
        self.__visual = "@"

    def set_health(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            result = self.__name + " повержен!"
            self.__name += " - мертв"
            self.__visual = "X"
        else:
            result = self.__health
        return result

    # Добавляем новых монстров в список для генерации
    def set_new_monsters(self, name):
        self.__monsters.append(name)

    # Добавляем новые "грейды" монстров
    def set_new_grade(self, grade):
        self.__grade_monsters.append(grade)

    def get_info(self):
        return "Название: "+self.__name+"\nЖизнь: "+str(self.__health)+"\nСила: "+str(self.__power)
