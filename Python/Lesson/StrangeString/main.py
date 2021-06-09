from conversion import Conversion


print("Введите какую-нибудь строку")
first_string = input()
print("И еще одну строку")
second_string = input()

new_first_string = Conversion(first_string)
new_second_string = Conversion(second_string)

print(new_first_string)
print(new_second_string)

print("Объединяем строки", new_first_string.concatenation(second_string))

print("Введите искомый символ")
symbol = input()

print("Ищем символ, он:", new_first_string.search_symbol(symbol))

new_first_string.compare_string(second_string)

print("Преобразуем лист в строку:", new_first_string.list_in_string())
