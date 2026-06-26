# do not change code below this line
import random
names = input( "Enter a list of names separated by commas: ")
name_list = names.split(", ")
# do not change code above  this line

# Write your code below this line
# To get total names in the list
total_names = len(name_list)

# To get randome number 
rand_num = random.randint(0, total_names - 1)
person_to_pay = name_list[rand_num]
print("\n")
print(person_to_pay + " is going to pay bill today")