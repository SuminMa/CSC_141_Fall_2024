# 9-13. Dice
# Make a class Die with one attribute called sides
from random import randint

class Die:
    def __init__(self):
        self.sides = 6

    def set_side(self, sides):
        self.sides = sides

    # Write a method prints a random number between 1 and the number of sides the die has.
    def roll_die(self):
        return randint(1, self.sides)

# Make a 6-sided die and roll it 10 times.
six_sided_die = Die()

for i in range (0, 10):
    print(six_sided_die.roll_die())

print() # New line

# Make a 10-sided die.
ten_sided_die =  Die()
ten_sided_die.set_side(10)

# Make a 20-sided die
twenty_sided_die = Die()
twenty_sided_die.set_side(20)

# Roll each die 10 times.
for i in range (0, 10):
    print(ten_sided_die.roll_die())

print() # New line

for i in range (0, 10):
    print(twenty_sided_die.roll_die())