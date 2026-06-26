# Don't Change code below line 
student_marks = [int(x) for x in input("Enter a list of students marks ").split()]
print(student_marks)
# Don't Change code above line
# Write your code below this line
total_marks = 0
for marks in student_marks:
  total_marks += marks
print(total_marks)

number_of_subjects = len(student_marks)
avg_marks = round(total_marks / number_of_subjects)
print("\n")
print(avg_marks)