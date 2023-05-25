test_numbers = []

for i in range(1,50):
    test_numbers.append(i)


def even_numbers(x):
    return x % 2 == 0


even_values = list(filter(even_numbers, test_numbers))

odd_values = list(filter(lambda a: a % 2 != 0, test_numbers))

print(odd_values)