# 10-9. Silent Cats and Dogs

"""Modify my except block in Exercise 10-8 to fail
silently if either file is missing."""
from pathlib import Path

cats_path = Path('cats.txt')
dogs_path = Path('dogss.txt')

cats_name = "Meow\nKitty\nChoco"
dogs_name = "Barky\nLily\nEric"

cats_path.write_text(cats_name)
# dogs_path.write_text(dogs_name)

try: 
    cats_contents = cats_path.read_text()
except FileNotFoundError:
    pass # Failing silently
else:
    print(f"cats.txt:\n{cats_contents}")

print() # Add a new line

try:
    dogs_contents = dogs_path.read_text()
except FileNotFoundError:
    pass # Failing silently
else:
    print(f"dogs.txt:\n{dogs_contents}")