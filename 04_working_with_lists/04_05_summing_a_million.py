#4-5. Summing a Million

#make a list of the numbers from one to one million
one_million = []
for i in range(1, 1000001):
    one_million.append(i)

#use min() and max() to make sure my list actually starts at one and ends at one million
print(min(one_million))
print(max(one_million))

#use the sum() function to see how quickly Python can add a million numbers
print(sum(one_million))