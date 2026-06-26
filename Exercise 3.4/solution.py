# don'n change code below line
print("Welcome to Python's Online Pizza Delievery!")
size = input("Which size of pizza would you like? S, M, or L: ").upper()
seasoning = input("Would you like seasoning? Y or N: ").upper()
extra_cheese = input("Would you like extra cheese? Y or N: ").upper()
# don't change code above line

# Write your code below this Line
bill = 0
if size == "S":
  bill += 60
elif size == "M":
  bill += 80
else:
  bill += 100

if seasoning == "Y":
  if size == "S":
    bill += 10
  elif size == "M":
    bill += 15
  else:
    bill += 20

if extra_cheese =="Y":
  bill += 30
print("\n")
message = f"You have ordered {size} size Pizza with seasoning = {seasoning} and extra cheese = {extra_cheese} Your Bill = ₹{bill}"
print(message)

