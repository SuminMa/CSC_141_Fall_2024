# 10-2. Learning C
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

# Replace the word Python with the name of another language.
lines = contents.splitlines()
for line in lines:
    # Print each modified line to the screen.
    print(line.replace("Python", "C"))