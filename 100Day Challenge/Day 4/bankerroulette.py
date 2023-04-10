# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number_of_person = len(names)
random_number = random.randint(0, number_of_person-1)
print(f"\n {names[random_number]} is going to buy the meal today!")
