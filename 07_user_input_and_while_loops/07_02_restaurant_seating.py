# 7-2. Restaurant Seating
# A program that asks the user how many people are in their dinner group
table_for = input("How many people are in your dinner group? ")
table_for = int(table_for)

# If answer is more than eight, print a message saying they'll have to wait
if table_for >= 8:
    print(f"\nYou might need to wait for a table for {table_for}. Is it okay?")

# Otherwise, report that their table is ready
else:
    print(f"\nA table for {table_for} is ready.")