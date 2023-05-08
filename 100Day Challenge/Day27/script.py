# this function takes in any number of arguments
def add(*args):
    sum_value = 0
    # type tuple
    for n in args:
        sum_value += n
    return sum_value


print(add(1, 2, 3, 4, 5, 6))


def calculate(n, **kwargs):
    # type dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get('color')


my_car = Car(make="Hyundai", model="Creta")

print(my_car.model, my_car.make)