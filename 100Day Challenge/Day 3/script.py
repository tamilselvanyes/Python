print("Welcome to the rollercoaster!!!")

height = int(input("What is your height in cms? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if (age >= 18):
        if (age >= 45 and age <= 55):
            bill = 0
        else:
            bill = 12
    elif (age > 12):
        bill = 7
    else:
        bill = 5
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"You have to pay {bill}.")
else:
    print("You can't ride the rollercoaster")
