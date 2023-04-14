import random
set_of_words = ["samples", "document", "energy", "temple"]

print("Welcome to Word Puzzle")
# generate the word
the_word = random.choice(set_of_words).lower()
list_of_words = [*the_word]

number_of_lives = 5
number_of_letters = len(list_of_words)

to_display = []


# generate the number of blanks
for i in range(0, number_of_letters):
    to_display.append("_")


def print_current_word(to_be_display):
    for i in range(0, number_of_letters):
        print(to_be_display[i], end=" ")


print_current_word(to_display)

while number_of_lives > 0:
    user_letter_choice = input("\n \n Guess a letter:")
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
        if (number_of_lives == 0):
            print(f"You lost the game the correct word is: {the_word}")
        else:
            print("Life lost, Remaining chances", number_of_lives)
