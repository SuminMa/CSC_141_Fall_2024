# The program's challenge is 1
"""
Reason: It was all good.
"""
# 10-4. Guest
# Write a program that prompts the user for their name.
from pathlib import Path

user_name = input("What is your name? ")

# When they respond, write their name to a file called guest.txt.
path = Path('guest.txt')
path.write_text(user_name)

# Test
contents = path.read_text()
print(contents)