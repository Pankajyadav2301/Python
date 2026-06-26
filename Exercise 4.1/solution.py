# Remember to Import Random Module
# Write your Code Below This Line
import random

coin_side = random.randint(0, 1)
if coin_side == 0:
    print("Tail")
else:
    print("Head")
