# this function takes in any number of arguments
def add(*args):
    sum_value = 0
    for n in args:
        sum_value += n
    return sum_value


print(add(1, 2, 3, 4, 5, 6))
