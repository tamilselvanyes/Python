import random

list = [1, 2, 3]

new_list = [n + 1 for n in list]

print(new_list)

name = "Tamil"

new_name = [letter for letter in name]

print(new_name)  # convert string to a list

new_range = [n * 2 for n in range(1, 5) if n % 2 == 0]
print(new_range)

names = ["Tamil", "Selvan", "Angela", "Japan", "Python"]

student_score = {item: random.randint(80, 100) for item in names}

print(student_score)

student_ninty_plus = { key: value for (key, value) in student_score.items() if value > 90}


print(student_ninty_plus)