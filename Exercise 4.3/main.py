# Don't Change code below this line
line1 = [" "," ", " "]
line2 = [" "," ", " "]
line3 = [" "," ", " "]
matrix = [line1,line2,line2]
print(f"{line1}\n{line2}\n{line3}")
pos = input("Where do you want to position X ?: ")
# Don't Change code above this line
# Write your code Below this Line
row = int(pos[0])
col = int(pos[1])
row_selected = matrix[row - 1]
row_selected[col - 1] = "X"


# Write your code above this Line
# Don't Change code below this line
print(f"{line1}\n{line2}\n{line3}")