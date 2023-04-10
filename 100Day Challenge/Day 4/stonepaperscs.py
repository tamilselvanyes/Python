import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
valid_choice = [rock, paper, scissors]
user_choice = int(
    input("what you want to choose 0 for Rock, 1 for Paper or 2 for scissors?"))

if (user_choice > 2 or user_choice < 0):
    print("Invalid input, you lose!")
else:
    print(valid_choice[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(valid_choice[computer_choice])
    if user_choice == computer_choice:
        print("Match drawn.")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose, try again.")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose, try again.")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose, try again.")
    elif user_choice == 2 and computer_choice == 1:
        print("You won.")
    elif user_choice == 1 and computer_choice == 0:
        print("You won.")
    elif user_choice == 0 and computer_choice == 2:
        print("You won.")
    else:
        print("Invalid inputs")
