# 10-14. Verify User
import json

def get_stored_username():
    """Get stored username if available."""
    try:
        with open('username.json', 'r') as f:
            username = json.load(f)
        return username
    except FileNotFoundError:
        return None

def get_new_username():
    """Prompt for a new username and store it."""
    username = input("What's your name? ")
    with open('username.json', 'w') as f:
        json.dump(username, f)
    return username

def verify_user(stored_username):
    """Ask the user if the stored username is correct."""
    is_correct_user = input(f"Is this you, {stored_username}? (yes/no): ").lower()
    if is_correct_user == 'yes':
        return True
    else:
        return False

def greet_user():
    """Greet the user by name, or ask for a new username."""
    username = get_stored_username()
    
    if username:
        if verify_user(username):
            print(f"Welcome back, {username}!")
        else:
            # Ask for a new username and store it
            username = get_new_username()
            print(f"We've updated your name to {username}. Welcome!")
    else:
        # If no username is stored, ask for a new one
        username = get_new_username()
        print(f"Welcome, {username}! We'll remember you next time.")

# Run the program to greet the user
greet_user()