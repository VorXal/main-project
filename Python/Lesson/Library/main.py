import author
import book

print("Добавить автора? (Y/N)")
open_editor = input()
if open_editor == "Y":
    flag = True
else:
    flag = False

author_id = 1
author_list = list()

while flag:
    print("Добавление автора. Введите имя:")
    name = input()
    print("Введите возраст:")
    age = int(input())
    print("Введите пол (Male/Female):")
    gender = input()
    print("Введите e-mail автора:")
    email = input()

    # Занесение в бд? Или в лист?
    new_author = author.Author(author_id, name, email, gender, age)
    author_id += 1
    author_list.append(new_author)

    print("Автор:", new_author, "добавлен")
    print("Добавить еще автора? (Y/N)")
    author_editor_exit = input()
    if author_editor_exit == "N":
        flag = False

# Создаем доп авторов в конструкторе
Nattzy = author.Author(2, "Лимонов Роман", "new.nattzy@gmail.com", "Male", 24)
Vorxal = author.Author(3, "Воронков Алексей", "vorxal@gmail.com", "Male", 21)

author_list.append(Nattzy)
author_list.append(Vorxal)

print(author_list)

# Создаем в конструкторе книги
Nolan = book.Book("Нолан", author_list, 400, "Первая")
Nolan.output_info()
