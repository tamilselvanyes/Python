import random
from random import randint
from random import *


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


# print(add(10, 20))
# print(sub(20, 10))
# print(sub(b=100, a=20))


list_1 = ["apple", "orange", "cucumber"]
list_2 = ["banana", "mango"]
# print(list_1 + list_2)

# list_2.append("apple")
# print(list_2[-2])
# -1 is the last element

letters = ["a", "b", "c", "d", "e", "f"]
# list slicing list[start:end] Start is included, but end is not.
# print(letters[1:4])


# Range: # range(start, end, step) end is not included
# for i in range(6, -6, -2):
# print(i)
# result: 6, 4, 2,0,-2,-4
# 0 is not included.


# randomisation

# n = random.randint(0, 6)
# n = randint(0, 10)
# n = choice(letters)
# print(n)
