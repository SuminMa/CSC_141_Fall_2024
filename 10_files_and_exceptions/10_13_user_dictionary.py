# 10-13. User Dictionary
import json

def get_stored_user_info():
    """Get stored user info if available."""
    try:
        with open('user_info.json', 'r') as f:
            user_info = json.load(f)
        return user_info
    except FileNotFoundError:
        return None

def store_user_info():
    """Prompt the user for their information and store it in a dictionary."""
    user_info = {}
    
    # Collect information
    user_info['name'] = input("What's your name? ")
    user_info['age'] = input("How old are you? ")
    user_info['favorite_color'] = input("What's your favorite color? ")
    
    # Save the dictionary to a file
    with open('user_info.json', 'w') as f:
        json.dump(user_info, f)
    
    return user_info

def show_user_info():
    """Display the user's stored information, or prompt for it if not available."""
    user_info = get_stored_user_info()
    
    if user_info:
        print("Here's what I remember about you:")
        print(f"Name: {user_info['name']}")
        print(f"Age: {user_info['age']}")
        print(f"Favorite color: {user_info['favorite_color']}")
    else:
        user_info = store_user_info()
        print("Thanks! I've stored your information.")

# Run the program to either retrieve or collect the user's info
show_user_info()