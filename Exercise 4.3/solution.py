# Don't Change code below this line
line1 = [" "," ", " "]
line2 = [" "," ", " "]
line3 = [" "," ", " "]
matrix = [line1,line2,line2]
print(f"{line1}\n{line2}\n{line3}")
pos = input("Where do you want to position X ?: ")
# Don't Change code above this line
# Write your code Below this Line
#23 number Entered
horizontal = int(pos[0]) #2
vertical = int(pos[1]) #3
row_selected = matrix[horizontal - 1]
row_selected[vertical - 1] = "X"
# Don't Change code below this line
print(f"{line1}\n{line2}\n{line3}")