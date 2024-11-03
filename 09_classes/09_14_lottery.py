# 9-14. Lottery
# Make a list containing a series of 10 numbers and 5 letters.
from random import choice

list = [138, 148, 39, 43, 51, 680, 730, 810, 909, 140, "A", "E", "X", "M", "Q"]
lottery = []

# Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
for i in range (0, 4):
    lottery.append(choice(list))

print(f"any ticket matching these {lottery} wins a prize.")

