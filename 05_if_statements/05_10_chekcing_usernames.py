#5-10. Checking Usernames

#Make a list of five or more usernames called current_users.
current_users = ['Sumin', 'Xavier', 'Maddie', 'Erica', 'Monica']
#Make another list of five usernames called new_users.
new_users = ['Charlotte', 'Sojin', 'Giuseppe', 'Erin', 'Wilson']
#Make sure one or two of the new usernames are also in the current_users list.
current_users.append('Charlotte')
current_users.append('Sojin')
#Loop through the new list to see if each new username has already been used.
for user in new_users:
    #If it has, print a message that the person will need to enter a new one.
    if user in current_users:
        print("It has already been used. You need to enter a new username.")
    #If it has not been used, print a message saying that it is available.
    else:
        print("It has not been used. You can use the username.")