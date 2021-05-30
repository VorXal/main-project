# 1) Write a Python program to iterate over sets (and multiply every element on 2)
print("Python program to iterate over sets (and multiply every element on 2)")


def set_multiplication(incoming_set):
    return {i*2 for i in incoming_set}


some_set = {1, 3, 5, 7, 1, 95, 4}
print("Data: ", some_set)
print("Result: ", set_multiplication(some_set), "\n")


# 2) Write a Python program to add member(s) in a set
print("Python program to add member(s) in a set")


def add_set_member(incoming_set, yet_incoming_set):
    return incoming_set.union(yet_incoming_set)


some_set = {1, 3, 5, 7, 1, 95, 4}
some_date = (5, 2, 234)
print("Data: ", some_set, "and", some_date)
print("Result: ", add_set_member(some_set, some_date), "\n")


# 3) Write a Python program to create an intersection of sets
print("Python program to create an intersection of sets")


def set_intersection(incoming_set, yet_incoming_set):
    return incoming_set.intersection(yet_incoming_set)


some_set = {1, 3, 5}
some_date = {5, 1, 234}
print("Data: ", some_set, "and", some_date)
print("Result: ", set_intersection(some_set, some_date), "\n")


# 4) Write a Python program to create a shallow copy of sets
print("Python program to create a shallow copy of sets")


def set_intersection(incoming_set):
    set_copy = incoming_set
    set_copy.add(44)
    return set_copy


some_set = {1, 3, 5}
print("Data: ", some_set)
print("Result: ", set_intersection(some_set))
print("Data: ", some_set)
