#2-11. Adding Comments

#write two of the programs and add at least one comment to each

'''program_01
written by: sumin
date: 4th Sep, 2024
description: asking for the user's name and greeting them
'''
#assign a question to a variable
q_name = "What is your name? "
#assign the user's input to a variable 
name = input(q_name)
#assign a greeting message to a variable
message = f"Nice to meet you, {name}!"
#print the message
print(message)

print("\n")

'''program_02
written by: sumin
date: 4th Sep, 2024
description: calculator for Fahrenheit to Celsius
'''
#assign a question for degrees in Fahrenheit to a variable
q_fah = "How cold is it in Fahrenheit? "
#assign the user's input to a variable
fah = int(input(q_fah))
#convert it to Celsius
cal_f_to_c = 5/9 * (fah - 32)
#assign a message to tell the user the degrees in Celsius
message = f"It's {cal_f_to_c} degrees Celsius."
#print the message
print(message)
