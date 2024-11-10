# The program's challenge is 1
"""
Reason: It was all good.
"""
# 10-5. Guest Book
from pathlib import Path

# Write a while loop that prompts users for their name.
loop = True
user_names = ''
while loop:
    # Collect all the names that are entered.
    user_name = input("What is your name? (Enter 'q' to quit.) ")
    if user_name == "q":
        loop = False
    else:
        user_names += user_name + "\n"
        
        
# Then write these names to a file called guest_book.txt.
path = Path('guest_book.txt')
path.write_text(user_names)

# Make sure each entry appears on a new line in the file.
contents = path.read_text()
print(contents)