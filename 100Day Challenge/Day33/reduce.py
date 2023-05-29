from functools import reduce
import datetime

list_of_numbers = []

for i in range(1, 10):
    list_of_numbers.append(i)

sum_of_list = reduce(lambda a, b: a + b, list_of_numbers)

print(sum_of_list)

tuple_one = (datetime.datetime(2023, 5, 9, 0, 0),
          datetime.datetime(2023, 5, 15, 23, 59, 59))

tuple_two = (datetime.datetime(2023, 5, 16, 0, 0),
          datetime.datetime(2023, 5, 22, 23, 59, 59))
print(tuple_one[1])