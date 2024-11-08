# 10-12. Favorite Number Remembered
import json

def get_stored_favorite_number():
    """Get the stored favorite number if it exists."""
    try:
        with open('favorite_number.json', 'r') as f:
            favorite_number = json.load(f)
        return favorite_number
    except FileNotFoundError:
        return None

def store_favorite_number():
    """Prompt for a new favorite number and store it."""
    favorite_number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def show_favorite_number():
    """Show the user's favorite number, retrieving it from the file or asking for it."""
    favorite_number = get_stored_favorite_number()
    
    if favorite_number:
        print(f"I know your favorite number! It’s {favorite_number}.")
    else:
        favorite_number = store_favorite_number()
        print(f"I'll remember your favorite number, it's {favorite_number}.")

# Call the function to run the program
show_favorite_number()
