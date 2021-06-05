import author


# Создаем в конструкторе автора - Tom
Tom = author.Author("Tom", "Tom@gmail.com", "Male", 35)
Tom.output_info()


# Меняем e-mail Toma
print("Введите свой e-mail")
Tom.email = input()


# Выводим информацию об авторе - Tom
Tom.output_info()
