import random
from stage_art import stages
from words import word_list
from hangman_log import logo


print(logo)
# generate the word
the_word = random.choice(word_list).lower()
list_of_words = [*the_word]

number_of_lives = 6
number_of_letters = len(list_of_words)

to_display = []
user_guesses = []


# generate the number of blanks
for i in range(0, number_of_letters):
    to_display.append("_")


def print_current_word(to_be_display):
    for i in range(0, number_of_letters):
        print(to_be_display[i], end=" ")


print_current_word(to_display)

while number_of_lives > 0:
    user_letter_choice = input("\n \n Guess a letter:")
    if (user_letter_choice in user_guesses):
        print("You have already guessed this letter", user_letter_choice)
        if user_letter_choice in the_word:
            print_current_word(to_display)
        else:
            print("We are not penalisied for this guess")
        print(stages[number_of_lives])
        continue
    if user_letter_choice in the_word:
        for index, letter in enumerate(list_of_words):
            if (letter == user_letter_choice):
                to_display[index] = user_letter_choice
        print_current_word(to_display)
        if ("_" not in to_display):
            print(f"You won,you have correctly guessed the word:{the_word}")
            break
    else:
        number_of_lives -= 1
        print(stages[number_of_lives])
    user_guesses.append(user_letter_choice)
