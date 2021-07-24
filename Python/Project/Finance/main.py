from user import User
from pymongo import MongoClient
from interaction import Interaction


if __name__ == "__main__":
    admin = User("Your Login", "Your Password")
    client = MongoClient(admin.get_connect())
    db = client.fincon
    spending = db.spending

    while True:
        print("Введите действие")
        action = input()
        if action == "Вывести все":
            print(Interaction.get_all(spending))
        elif action == "Добавить":
            print("Введите название")
            name = input()
            print("Введите тип")
            type = input()
            print("Введите цену")
            cost = int(input())
            Interaction.insert(spending, name, type, cost)
        else:
            print("Команда не распознана")
