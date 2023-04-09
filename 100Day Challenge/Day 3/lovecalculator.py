# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t_count = lower_name1.count("t") + lower_name2.count("t")
r_count = lower_name1.count("r") + lower_name2.count("r")
u_count = lower_name1.count("u") + lower_name2.count("u")
e_count = lower_name1.count("e") + lower_name2.count("e")

tenth_digit = t_count + r_count + u_count + e_count

l_count = lower_name1.count("l") + lower_name2.count("l")
o_count = lower_name1.count("o") + lower_name2.count("o")
v_count = lower_name1.count("v") + lower_name2.count("v")

oneth_digit = l_count + o_count + v_count + e_count

score = tenth_digit * 10 + oneth_digit

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40 and score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
