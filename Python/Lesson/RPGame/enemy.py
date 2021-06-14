import random


class Enemy:

    def __init__(self, hero_level):
        self.__level = random.randrange(hero_level, hero_level+2)
        self.__monsters = ["Демон", "Гоблин", "Скелет", "Суккуб", "Вервольф"]
        self.__grade_monsters = ["Младший ", "Старший ", "Архи-"]
        rand_m = random.randrange(0, len(self.__monsters))
        rand_g = random.randrange(0, len(self.__grade_monsters))
        if rand_g == 1:
            self.__level += 3
        elif rand_g == 2:
            self.__level += 10
        self.__name = self.__grade_monsters[rand_g] + self.__monsters[rand_m]
        self.__health = self.__level * random.randrange(50, 100)
        self.__power = self.__level + random.randrange(20, 40)
        self.__visual = "@"

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_power(self):
        return self.__power

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
