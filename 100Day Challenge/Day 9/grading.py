student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
def getGrading(score):
    if score <= 70:
        return "Fail"
    elif score > 70 and score <= 80:
        return "Acceptable"
    elif score > 80 and score <= 90:
        return "Exceeds Expectations"
    else:
        return "Outstanding"


for name in student_scores:
    student_grades[name] = getGrading(student_scores[name])


# 🚨 Don't change the code below 👇
print(student_grades)
