from art import logo


print(logo)
secret_aution = {}
bidding_finish = False


def add_bidder(name, bidding_price):
    secret_aution[name] = bidding_price


def get_winner():
    winner = ""
    highest_bidding_price = 0
    for name in secret_aution:
        if secret_aution[name] > highest_bidding_price:
            winner = name
            highest_bidding_price = secret_aution[name]
    print(
        f"Winner of the bidding is {winner} and the bidding amount is {highest_bidding_price}")


while (not bidding_finish):
    name = input("Please enter your name:")
    bid_price = int(input("Please enter your biding price $:"))
    add_bidder(name, bid_price)
    continue_bidding = input("Is there any bidder left? if 'yes' or 'no'")
    if (continue_bidding == 'yes'):
        continue
    else:
        bidding_finish = True
        get_winner()
