# Don't change the code below line

year = int(input("Enter a year: "))

# Don't change the code above line

# Write your code below this line
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")