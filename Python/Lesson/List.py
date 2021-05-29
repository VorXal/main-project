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
