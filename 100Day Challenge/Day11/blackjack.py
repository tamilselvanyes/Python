
import random
card_choices = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_total(list):
    if (sum(list) == 21 and len(list) == 2):
        return 0
    if (11 in list and sum(list) > 21):
        list.remove(11)
        list.append(1)
    return sum(list)


def compare(user_total, computer_total):
    if (user_total == computer_total):
        return "Match drawn 🤪"
    elif (user_total == 0):
        return "You won with a Black Jack😎"
    elif (computer_total == 0):
        return "Computer won with a White Jack 😤"
    elif (user_total > 21 and computer_total < 21):
        return "You went over you lost😭"
    elif (user_total < 21 and computer_total > 21):
        return "Computer went over you won😇"
    elif (user_total < computer_total):
        return "You lost 😭"
    else:
        return "You won😍"


def start_game():
    user_cards = random.choices(card_choices, k=2)
    computer_cards = random.choices(card_choices, k=2)
    user_withdrawn = False
    computer_withdrawn = False
    game_over = False
    if (calculate_total(user_cards) == 0):
        game_over = True

    while ((not user_withdrawn or not computer_withdrawn) and not game_over):
        print(
            f"Your cards:{user_cards}, current score: {calculate_total(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        if (not user_withdrawn):
            draw_card_input = input(
                "Type 'y' to get another card, type 'n' to pass:")
            if (draw_card_input == "y"):
                draw_random = random.choice(card_choices)
                user_cards.append(draw_random)
                current_total = calculate_total(user_cards)
                if (current_total > 21):
                    game_over = True
                    break
            else:
                user_withdrawn = True
                if (computer_withdrawn):
                    game_over = True
        if (not computer_withdrawn):
            if (calculate_total(computer_cards) < 17 and calculate_total != 0):
                draw_com_random = random.choice(card_choices)
                computer_cards.append(draw_com_random)
                current_total = calculate_total(computer_cards)
                if (current_total > 21):
                    game_over = True
                    break
            else:
                computer_withdrawn = True
                if (user_withdrawn):
                    game_over = True

    if (game_over):
        grand_user_total = calculate_total(user_cards)
        grand_computer_total = calculate_total(computer_cards)
        print(f"Your final hand {user_cards} and total {grand_user_total}")
        print(
            f"Computer final hand {computer_cards} and total {grand_computer_total}")
        print(compare(grand_user_total, grand_computer_total))

    play_again = input("You want to play Black Jack again 'y' or 'n'")
    if (play_again == 'y'):
        start_game()


start_game()
