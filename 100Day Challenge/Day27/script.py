# this function takes in any number of arguments
def add(*args):
    sum_value = 0
    # type tuple
    for n in args:
        sum_value += n
    return sum_value


print(add(1, 2, 3, 4, 5, 6))


def calculate(**kwargs):
    # type dictionary
    print(kwargs)


calculate(add=3, multiply=5)
