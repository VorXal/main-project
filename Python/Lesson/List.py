# Write a Python program to sum all the items in a list
print("Python program to sum all the items in a list")


def sum_items(array):
    summa = 0
    for i in array:
        summa += array[i]
    return summa


some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_items(some_list))


# 2) Write a Python program to remove duplicates from a list.
print("Python program to remove duplicates from a list")


def delete_duplicate(array):
    array = set(array)
    array = list(array)
    return array


duplicate_list = [7, 1, 1, 3, 4, 4, 6, 7, 8, 4]
print(delete_duplicate(duplicate_list))


# 3) Write a Python program to append a list to the second list.
print("Python program to append a list to the second list")


def list_append(first_list, second_list):
    new_list = []
    for i in first_list:
        new_list.append(i)
    for i in second_list:
        new_list.append(i)
    return new_list


some_list = [1, 5, 3, 6]
yet_some_list = [1, 5, 3, 2, 5, 6]
print(list_append(some_list, yet_some_list))

# Или 2 вариант

some_list = [1, 5, 3, 6]
yet_some_list = [1, 5, 3, 2, 5, 6]
some_list.extend(yet_some_list)
print(some_list)


# 4) Write a Python program to compute the difference between two lists.
#               Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
#               Expected Output:
#                             Color1-Color2: ['white', 'orange', 'red']
#                             Color2-Color1: ['black', 'yellow']
print("Python program to compute the difference between two lists\n")


def search_difference(first_list, second_list):
    buffer = []
    for i in second_list:
        buffer.append(i)

    for i in first_list:
        index_first = first_list.index(i)
        for j in second_list:
            index_second = second_list.index(j)
            if first_list[index_first] == second_list[index_second]:
                first_list.remove(first_list[index_first])
                buffer.remove(second_list[index_second])

    first_list.reverse()

    print("Color1-Color2: ", first_list)
    print("Color2-Color1: ", buffer)


#   return first_list, buffer


Color1 = ["red", "orange", "green", "blue", "white"]
Color2 = ["black", "yellow", "green", "blue"]

search_difference(Color1, Color2)


# print("Color1-Color2: ", Color1)
# print("Color2-Color1: ", Color2)


# 5) Write a Python program to move all zero digits to end of a given list of numbers.
#               Expected output:
#                             Original list:
#                             [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
#                             Move all zero digits to end of the said list of numbers:
#                             [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Python program to move all zero digits to end of a given list of numbers")


def move_zero(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array


some_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
print(move_zero(some_list))
