# The program's challenge is 7
"""
Reason: I was struggling a little to make the code clean before I found that
the splitlines function returns a list of the lines in the string.
"""
# 10-1. Learning Python
# Write a program that reads the file.

# Prints what I wrote two times.
# 1. Print the contents once by reading in the entire file.
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print() # Add a new line

# 2. And once by storing the lines in a list and then looping over each line.
lines = contents.splitlines() #Return a list of the lines in the string
for line in lines:
    print(line)