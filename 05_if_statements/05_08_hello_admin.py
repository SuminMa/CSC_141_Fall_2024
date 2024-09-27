#5-8. Hello Admin
#Make a list of five usernames, including the name 'admin'.
usernames = ['Sumin', 'Xavier', 'Erica', 'Monica', 'admin']
#Loop through the list, and print a greeting to each user.
for user in usernames:
    #If the username is 'admin', print a special greeting
    if (user == 'admin'):
        print("Hello admin, would you like to see a status report?")
    #Otherwise, print a generic greeting
    else:
        print(f"Hello {user}, thank you for logging in again.")