#4-15. Code Review

'''Choose three of the programs I've written in this chapter and modify each
one to comply with PEP 8
1. Use four spaces for each indentation level
2. Use less than 80 characters on each line
3. Don’t use blank lines excessively in your program files'''
#[01] 4-1. Pizzas
#store these pizza names in a list
pizzas = ['pineapple', 'cheese', 'meat']
#use a for loop to print the name of each pizza
for pizza in pizzas:
    print(pizza)
print() #add a new line
#modify my for loop to print a sentence using the name of the pizza
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print() #add a new line
'''add a line at the end of my program, outside the for loop, that states how
much I like pizza'''
print("I absolutely love all of those!")

#[02] 4-5. Summing a Million
#make a list of the numbers from one to one million
one_million = []
for i in range(1, 1000001):
    one_million.append(i)
'''use min() and max() to make sure my list actually starts at one and ends at
one million'''
print(min(one_million))
print(max(one_million))
#use the sum() function to see how quickly Python can add a million numbers
print(sum(one_million))

#[03] 4-6. Odd Numbers
'''use the third argument of the range() function to make a list of the odd
numbers from 1 to 20'''
odd_nums = range(1, 21, 2)
#use a for loop to print each number
for num in odd_nums:
    print(num)