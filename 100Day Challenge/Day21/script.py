class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()

# list slicing::
paino_keys = ["a", "b", "c", "e", "f", "g"]

print(paino_keys[2:5])  # ['c', 'e', 'f']
print(paino_keys[2:])  # ['c', 'e', 'f', 'g']
print(paino_keys[:2])  # ['a', 'b']
print(paino_keys[2:5:2])  # ['c', 'f'] every second in the range
print(paino_keys[::2])  # every second element
print(paino_keys[::-1])  # reverse the order of the list
