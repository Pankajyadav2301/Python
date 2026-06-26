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
student_grades = {}

# TASK2- write code below to add grades
for students in student_marks:
    marks =student_marks[students] 
    if marks > 90:
        student_grades[students] = "A++"
    elif marks > 80:
        student_grades[students] = "A+"
    elif marks > 70:
        student_grades[students] = "A"
    else:
        student_grades[students] = "Fail"

# do not change code above this line
print(student_grades)