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
    for i in array:
        print("i = ", i)
        for j in array[1::]:
            print("j = ", j)
            if array[i] == array[j]:
                print("WHATS WRONG WITH YOU?")


duplicate_list = [7, 1, 1, 3, 4, 4, 6, 7, 8, 4]
print(delete_duplicate(duplicate_list))
