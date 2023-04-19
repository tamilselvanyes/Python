import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinkng of a number between 1 and 100")


def set_difficulty():
    difficulty = input("Choose difficulty. Type 'easy' or 'hard':")
    if (difficulty == "easy"):
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def play_game():
    print("Welcome to the Number Guessing Game")
    print("I am thinkng of a number between 1 and 100")
    correct_number = random.randint(1, 100)
    no_of_attempts = set_difficulty()
    no_of_guesses = 0

    while (no_of_attempts > 0):
        if (no_of_guesses != 0):
            print("Guess again")
        print(f"You have {no_of_attempts} attempts to guess the number")
        guess = int(input("Make a guess: "))
        if (guess == correct_number):
            print(
                f"You got it in {no_of_guesses} guesses! The answer was {correct_number}")
            return
        elif (guess > correct_number):
            print("Too high")
            no_of_attempts -= 1
        else:
            print("Too low")
            no_of_attempts -= 1
        no_of_guesses += 1
    if (no_of_attempts == 0):
        print("You've run out of guesses, you lose")


play_game()
