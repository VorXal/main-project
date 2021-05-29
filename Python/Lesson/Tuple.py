# 1) Write a Python program to add an item in a tuple
print("Python program to add an item in a tuple")

word = input()
item = input()

some_tuple = tuple(word)
some_tuple = list(some_tuple)
some_tuple.append(item)
some_tuple = tuple(some_tuple)

print("New tuple: ", some_tuple)


