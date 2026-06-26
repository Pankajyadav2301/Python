# Do not change the code below
height = float(input("Enter Your Height in Meters : "))
weight = int(input("Enter Your Weight in Kg. : "))

bmi = round(weight / height ** 2, 2)

# Do not change the code above

# Write your code below this line
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are Obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")