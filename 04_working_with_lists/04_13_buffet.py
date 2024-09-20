#4-13. Buffet

#store five simple foods in a tuple
buffet = ('fried chicken', 'french fries', 'potato chips', 'chocolate', 'ice cream')

#use a for loop to print each food the restaurant offers
for food in buffet:
    print(f"The restaurant offers {food}.")

#try to modify one of the items, and make sure that Python rejects the change
#buffet[0] = 'cucumber'

#add a line that rewrites the tuple to replace two of the items with different foods
buffet = ('fried rice', 'basil pasta', 'potato chips', 'chocolate', 'ice cream')

#use a for loop to print each of the items on the revised menu
print("\nThe restaurant changes its menu... Here's the new menu:")
for food in buffet:
    print(f"\t{food}")