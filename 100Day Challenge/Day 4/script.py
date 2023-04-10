# Random module.
# MersenneTwister
import random
import my_module

random_int = random.randint(1, 100)
# random method always return a random number between 0 and 1(not inclusive)
random_float = random.random() * 5
# print(random_int, my_module.user)
# print(random_float)

# python lists
fruits = ['apple', 'orange', 'banana', 'grapes', 'strawberry']
fruits.append("watermelon")
fruits.extend(["kiwi", "blueberry"])

vegies = ["beetroot", "carrot", "beans", "brinjal"]

# print(fruits)

# indexError: list our of range eg: fruits[100]
# nested list
