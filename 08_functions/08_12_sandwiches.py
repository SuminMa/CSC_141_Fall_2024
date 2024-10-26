# 8-12. Sandwiches

# Write a function that accepts a list of items a person wants on a sandwich.
# It should have one parameter that collects as many items as the function call provides.
def make_sandwich(*items):
    """Summarize the sandwiches we are about to make"""
    # It should print a summary of the sandwich that's being ordered.
    print("\n Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times, using a different number of arguments each time.
make_sandwich('tomato')
make_sandwich('tomato', 'cheese')
make_sandwich('tomato', 'cheese', 'chicken')