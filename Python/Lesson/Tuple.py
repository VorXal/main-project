# 1) Write a Python program to add an item in a tuple
print("Python program to add an item in a tuple")

word = input()
item = input()

some_tuple = tuple(word)
some_tuple = list(some_tuple)
some_tuple.append(item)
some_tuple = tuple(some_tuple)

print("New tuple: ", some_tuple)


# 2) Write a Python program to convert a list to a tuple
print("Python program to convert a list to a tuple")
some_list = [1, 2, 3, 4, 5]
some_list = tuple(some_list)


# 3) Find the index of an item of a tuple
print("Python program find the index of an item of a tuple")


def find_index(array, num):
    answer = 'false'
    for i in array:
        if i == num:
            answer = 'true'
    if answer == 'true':
        result = array.index(num)
        return result
    else:
        print("ERROR:", num, " - нет в tuple")


sentence = [1, 2, 3, 5, 10]
sentence = tuple(sentence)
number = int(input())

print("Result: ", find_index(sentence, number))


# 4) Write a Python program to reverse a tuple
print("Python program to reverse a tuple")


# 5) Write a Python program to remove an item from a tuple
print("Python program to remove an item from a tuple")
