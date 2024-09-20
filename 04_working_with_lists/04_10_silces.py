#4-10. Slices

#using one of the programs I wrote in this chapter
cubes = [value**3 for value in range(1, 11)] #from exercise 04-09

#use a slice to print the first three itmes from that program's list
print(cubes[:3])

#use a slice to print the middle three itmes from that program's list
print(cubes[3:6])

#use a slice to print the last three itmes from that program's list
print(cubes[-3:])
