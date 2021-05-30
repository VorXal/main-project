# Задание 1. Сортировка
# Дан массив целых чисел. Напишите функцию, которая получает данный массив в
# качестве аргумента и сортирует его по возрастанию
print("Сортировка")


def sort_list(array):
    return sorted(array)


some_list = [3, 5, 7, 1, 2, 60]
print("Data: ", some_list)
print("Result: ", sort_list(some_list), "\n")


# Задание 2. Поиск
# Напишите функцию, которая для отсортированного маcсива целых чисел
# определяет, содержится ли в нем заданное значение
print("Поиск")


def check_list(array, num):
    buffer = sorted(array)
    for i in buffer:
        if i == num:
            print("Result:", buffer, "содержит", num, "\n")
            return 0
    print("Result:", buffer, "не содержит", num, "\n")


number = 3
some_list = [3, 5, 7, 1, 2, 60]
print("Data: ", some_list, "and", number)
check_list(some_list, number)

# Задание 3. Строки
# Дана строка, вывести только те слова, которые встречаются в ней только один раз
print("Строки")


# Задание 4 Факториал
# Написать функцию нахождения факториала числа n
print("Факториал")


def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


number = 7
print(factorial(number))

# Задание 5. Правильная скобочная последовательность
# Дана строка состоящая из скобок “{},(),[]”, определить является ли данная строка
# правильно скобочной последовательность. Например (()) – псп, а ((() нет
print("\nПравильная скобочная последовательность")
