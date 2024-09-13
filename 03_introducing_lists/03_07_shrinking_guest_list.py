#3-7. Shrinking Guest List

#start with 3-6
guest_list = ['Maddie', 'Xavier', 'Emily', 'Erica', 'Monica', 'Jeily', 'Sojin']

#add a new line that prints a message saying that I can ivite only two people for dinner
print("I can only invite two people to dinner after all")

#initialize integers for use in a while loop
i = 0
j = 0

#use pop() to remove guests from my list one at a time until only two names remain in my list
while i < 5:
    not_invited = guest_list.pop()
    print(f"I'm so sorry, {not_invited}. I can't invite you.") #print a message to the person letting them know I'm sorry you can't invite them to dinner
    i += 1
print() #add a new line

#print a message to each of the two people still on my list, letting them know they're still invited
for invited in guest_list:
    print(f"Hello, {invited}. You're invited if you're interested.")
print() #add a new line

#use del to remove the last two names from my list, so I have an empty list
while j < len(guest_list):
    del guest_list[j]

#print my list to make sure I actually have an empty list
print(guest_list)