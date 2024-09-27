#5-6. Stages of Life
#Write an if-elif-else chain that determines a person’s stage of life
def stage_of_life(age):
    if (age < 2):
        print("\nThe person is a baby.")
    elif (2 <= age < 4):
        print("\nThe person is a toddler.")
    elif (4 <= age < 13):
        print("\nThe person is a kid.")
    elif (13 <= age < 20):
        print("\nThe person is a teenager.")
    elif (20 <= age < 65):
        print("\nThe person is an adult.")
    else:
        print("\nThe person is an elder.")

#Write every versions of the program
stage_of_life(1) #a baby
stage_of_life(2) #a toddler
stage_of_life(5) #a kid
stage_of_life(15) #a teenager
stage_of_life(23) #an adult
stage_of_life(90) #an elder
