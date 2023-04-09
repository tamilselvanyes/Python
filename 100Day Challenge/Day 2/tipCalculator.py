# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator")

total_bill_as_int = float(input("What was the total bill? $"))


tip_percent_as_int = int(input(
    "What percentage tip would you like to give? 10, 12, or 15?"))

number_of_people_as_int = int(input("How many people to split the bill?"))

# calculation

total_amount_paid = total_bill_as_int * (1 + tip_percent_as_int/100)

print(
    f"Each person should pay:${round(total_amount_paid/number_of_people_as_int, 2)}")
