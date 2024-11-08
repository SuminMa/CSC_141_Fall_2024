# 10-3. Simpler Code

"""We can skip the temporary variable and loop directly
over the list that splitlines() returns:"""

# Remove the temporary variable from each of the programs in this section,
# to make them more concise.

# 10-1. Learning Python
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print()

for line in contents.splitlines(): # Remove the temporary variable.
    print(line)

# 10-2. Learning C
print()

for line in contents.splitlines(): # Remove the temporary variable.
    print(line.replace("Python", "C"))