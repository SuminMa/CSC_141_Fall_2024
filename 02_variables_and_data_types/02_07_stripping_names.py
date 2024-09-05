#2-7. Stripping Names

##use a variable to represent a person's name including some whitespace characters,\t \n
name = "    fruits i like:\n\tapples\n\tbanana\n\tgrapes     "

#print the name so the whitespace around the name is displayed
print(name)

#add string "|" on the left side to see the result of the function called 'lstrip'
#print the name using the function called lstrip()
print(name.lstrip()+"|")

#print the name using the function called rstrip()
print(name.rstrip()+"|")

#print the name using the function called strip()
print(name.strip()+"|")