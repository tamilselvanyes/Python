# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
average = 0
total = 0
number_of_heights = 0

for student_height in student_heights:
    total += int(student_height)
    number_of_heights += 1

average = round(total / number_of_heights)

print(average)
