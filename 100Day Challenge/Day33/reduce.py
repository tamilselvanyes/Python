from functools import reduce

list_of_numbers = []

for i in range(1, 10):
    list_of_numbers.append(i)

sum_of_list = reduce(lambda a, b: a + b, list_of_numbers)

print(sum_of_list)
