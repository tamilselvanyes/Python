from art import logo, vs
import random
from game_data import data


already_listed = []
current_score = 0


def pick_one():
    new_one = False
    while (not new_one):
        random_pick = random.choice(data)
        if random_pick not in already_listed:
            new_one = True
            already_listed.append(random_pick)
            return random_pick


def compare(a, b, user_choice):
    winner = {}
    if (a["follower_count"] > b["follower_count"]):
        winner = a
    else:
        winner = b
    if (user_choice == winner):
        global current_score
        current_score += 1
        print(f"You'r are right, you current score: {current_score}")
        return True
    else:
        print(f"Sorry, you are wrong, you're final score:{current_score}")
        return False


def play_game():
    should_continue = True
    choice_one = pick_one()

    while should_continue:
        choice_two = pick_one()
        print(logo)
        print(
            f"Compare A: {choice_one['name']}, a {choice_one['description']} from {choice_one['country']}")

        print(vs)

        print(
            f"Against B: {choice_two['name']}, a {choice_two['description']} from {choice_two['country']}")

        user_choice = input("Who has more followers on instagram 'A' or 'B'")
        if (user_choice == 'A'):
            should_continue = compare(choice_one, choice_two, choice_one)
        else:
            should_continue = compare(choice_one, choice_two, choice_two)
        choice_one = choice_two


play_game()
