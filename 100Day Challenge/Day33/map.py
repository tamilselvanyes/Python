list_of_numbers = []

for i in range(1, 20):
    list_of_numbers.append(i)


def mul(a):
    return a * 2


result = list(map(mul, list_of_numbers))

print(result)