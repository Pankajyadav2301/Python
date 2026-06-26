student_marks = {
    "Sushma": 88,
    "Vinit": 76,
    "Aasha": 67,
    "Saurabh": 75,
    "Aniket": 99
}
# do not change code above this line
# Write your code below this line
# TASK1- creat an empty dictionary students_grades
students_grades = {}

# TASK2- write code below to add grades
for student in student_marks:
    marks = student_marks[student]
    if marks > 90:
        students_grades[student] = "A++"
    elif marks > 80:
        students_grades[student] = "A+"
    elif marks > 70:
        students_grades[student] = "A"
    else:
        students_grades[student] = "Fail"

# do not change code above this line
print(students_grades)