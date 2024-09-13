#3-10. Every Function

#things I could store in a list
fav_list = ['pink', 'sweets', 'flowers', 'letters', 'programming', 'love']
'''
write a program that creates the list containing these items and then
uses each function introduced in this chapter at least once.
'''

#the title() method also applies to the list
print(fav_list[0].title())
print() #add a new line

#the append() method to add a new element at the end of the list
fav_list.append('friends')
print(fav_list) #print the list with a new element added
print() #add a new line

#the insert() method to add a new element at any position in my list
fav_list.insert(0, 'family') #print the list with a new element added
print(fav_list) #print the list with a new element added
print() #add a new lin

#the del statement to remove a item from the list
del fav_list[2]
print(fav_list) #print the list with the third element deleted
print() #add a new line

#the pop() method to remove the last item in the list
fav_list.pop()
print(fav_list) #print the list with the last element deleted
print() #add a new line

#the remove() method to remove a value of the itme I want to remove from the list
fav_list.remove('flowers')
print(fav_list) #print the list with the last element deleted
print() #add a new line

#the sort() method to make it realatively easy to sort the list
fav_list.sort()
print(fav_list) #print the list sorted
print() #add a new line

#the sorted() function to maintain the original order of the list but present it in a sorted order
print(sorted(fav_list))
print() #add a new line

#the reverse() method to reverse the original order of the list
fav_list.reverse()
print(fav_list) #print the list reversed
print() #add a new line

#the len() function to find the length of the list
print(f"the length of the list is {len(fav_list)}.")
