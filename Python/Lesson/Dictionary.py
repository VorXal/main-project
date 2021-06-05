# 1) Write a Python program to iterate over dictionaries using for loops
print("Python program to iterate over dictionaries using for loops")


def iterate_dictionaries(dictionaries):
    for key in dictionaries:
        print(key, "- это", dictionaries.get(key))


elements = {"Au": "Золото", "Fe": "Железо", "H": "Водород", "O": "Кислород"}
iterate_dictionaries(elements)


# 2) Write a Python script to concatenate following dictionaries to create a new one
#              Sample Dictionary :
#                            dic1={1:10, 2:20}
#                            dic2={3:30, 4:40}
#                            dic3={5:50,6:60}
#              Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Python script to concatenate following dictionaries to create a new one")
import copy

def dict_concatenate(first_dict, *other_dict):
    result = first_dict.copy()
    for i in other_dict:
        result.update(i)
    return result

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

print("Data: ", dict1, dict2, dict3)
print("Result: ", dict_concatenate(dict1, dict2, dict3))


# 3) Write a Python program to sum all the items in a dictionary
print("Python program to sum all the items in a dictionary")


def sum_dictionary_elem(some_dict):
    return sum(some_dict[key] for key in some_dict)


dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Data: ", dictionary)
print("Result: ", sum_dictionary_elem(dictionary), "\n")


# 4) Write a Python program to multiply all the items in a dictionary
print("Python program to multiply all the items in a dictionary")


def multiply_dictionary_elem(some_dict):
    result = 1
    for value in some_dict.values():
        result *= value
    return result


dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Data: ", dictionary)
print("Result: ", multiply_dictionary_elem(dictionary))
