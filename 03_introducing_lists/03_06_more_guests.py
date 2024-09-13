#3-6. More Guests

#start with exercies 3-5
guest_list = ['Xavier', 'Erica', 'Monica', 'Jeily']

#add a print() call, infroming people that I found a bigger table
print(f"There is a bigger table.")
print() #add a new line

#use insert() to add one new guest to the beginning of my list
guest_list.insert(0, 'Maddie')

#use insert() to add one new guest to the middle of my list
guest_list.insert(2, 'Emily')

#use append() to add one new guest to the end of my list
guest_list.append('Sojin')

#print a new set of invitation messages, one for each person in my list
for new_list in guest_list:
    msg = f"Hello {new_list}, you're on my new guest list. I would like to invite you to dinner if you're interested!"
    print(msg)