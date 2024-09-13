#3-8. Seeing the World

#store the locations in a list
places = ['Paris', 'Colorado', 'California', 'Tokyo', 'London']

#print my list in its original order
print(places)

#use sorted() to print my list in alphabetical order without modifying the actual list
print(sorted(places))

#show that my list is still in its original order by printing it
print(places)

#use sorted() to print my list in reverse-alphabetical order without changing the order of the original list
print(sorted(places, reverse=True))

#show that my list is still in its original order by printing it again
print(places)

#use reverse() to change the order of my list
places.reverse()
#print the list to show that its order has changed
print(places)

#use reverse() to change the order of my list again
places.reverse()
#print the list to show it's back to its original order
print(places)

#use sort() to change my list so it's stored in alphabetical order
places.sort()
#print the list to show that its order has been changed
print(places)

#use sort() to change my list so it's stored in reverse-alphabetical order
places.sort(reverse=True)
#print the list to show that its order has changed
print(places)


