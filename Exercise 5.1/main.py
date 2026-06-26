# Don't Change code below line 
student_marks = [int(x) for x in input("Enter a list of students marks ").split()]
print(student_marks)
# Don't Change code above line
# Write your code below this line
total_marks = 0
for marks in student_marks:
  total_marks += marks

print(total_marks)
total_subject = len(student_marks)
print(total_subject)

avg_marks = round(total_marks / total_subject)
print(avg_marks)