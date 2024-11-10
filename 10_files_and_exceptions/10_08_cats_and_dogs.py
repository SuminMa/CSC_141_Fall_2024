# The program's challenge is 5
"""
Reason: It doesn't look good since it seems like there is a lot of repetitive code.
"""
# 10-8. Cats and Dogs
# Make two files, cats.txt and dogs.txt.
# Wrap your code in a try-except block to catch the FileNotFound error.
from pathlib import Path

cats_path = Path('cats.txt')
"""Make the files a different location on the system,
and make sure the code in the except block executes properly."""
dogs_path = Path('dogss.txt')

cats_name = "Meow\nKitty\nChoco"
dogs_name = "Barky\nLily\nEric"

# Store at least three names of cats in the first file.
cats_path.write_text(cats_name)
# And three names of dogs in the second file.
# dogs_path.write_text(dogs_name)

# Write a program that tries to read these files.
try: 
    cats_contents = cats_path.read_text()
except FileNotFoundError:
    # Print a friendly message if a file is missing.
    print(f"Sorry, the file '{cats_path}' does not exist.")
else:
    # And print the contents of the file to the screen.
    print(f"cats.txt:\n{cats_contents}")

print() # Add a new line

try:
    dogs_contents = dogs_path.read_text()
except FileNotFoundError:
    # Print a friendly message if a file is missing.
    print(f"Sorry, the file '{dogs_path}' does not exist.")
else:
    print(f"dogs.txt:\n{dogs_contents}")