# don't change the code below line
age = input("Enter your current age : ")
# don't change the code above line

# Write your code below this line

your_age = int(age)
years_left = 100 - your_age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

message = f"You have {years_left} Years, {months_left} Months, {weeks_left} Weeks and {days_left} Days left."

print("\n")
print(message)