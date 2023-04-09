# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

total_days = 90 * 365
total_weeks = 90 * 52
total_months = 90 * 12

days_already_spent = int(age) * 365
weeks_already_spent = int(age) * 52
months_already_spent = int(age) * 12

remaining_days = total_days - days_already_spent
remaining_weeks = total_weeks - weeks_already_spent
remaining_months = total_months - months_already_spent

print(
    f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
