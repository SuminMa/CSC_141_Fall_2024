# 6-5. Rivers
# Make a dictionary containing three major rivers and the country each river runs through
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}

# Use a loop to print a sentence about each river
for river in rivers:
    print(f"The {river.title()} runs through {rivers[river].title()}.")

# Use a loop to print the name of each river included in the dictionary
for river in rivers:
    print(f"The {river.title()}")

# Use a loop to print the name of each country included in the dictionary
for river in rivers:
    print(rivers[river].title())