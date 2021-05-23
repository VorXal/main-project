# Write a Python program to sum all the items in a list
print("Python program to sum all the items in a list")


def sum_items(array):
    summa = 0
    for i in array:
        summa += array[i]
    return summa


some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_items(some_list))
