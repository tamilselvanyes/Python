# scope of variables
# there is no block scope in python

# no block scope example:
# Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it


a = 5

if a > 4:
    b = a
print(b)


################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


game_level = 3
enemies = ["Zombie", "Skeleton", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


# Modifying the global variable within a local function

enemies = 1


def increase_enemies():
    global enemies
    enemies += 2
    print(enemies)


increase_enemies()


def increase_enemies_global():
    return enemies + 1


enemies = increase_enemies_global()

print(enemies)


# Global constants:

# Define in capital letters for global constants
PI = 3.14
