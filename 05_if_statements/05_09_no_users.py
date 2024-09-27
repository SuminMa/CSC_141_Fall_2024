#5-9. No Users
#Add an if test to hello_admin.py to make sure the list of users is not empty.
#Remove all of the usernames from my list
usernames = []
if usernames:
    for user in usernames:
        print(f"Hello, {user}!")
else:
    #If the list is empty, print the message We need to find some users!
    print("We need to find some users!")