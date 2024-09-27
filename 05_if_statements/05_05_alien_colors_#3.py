#5-5. Alien Colors #3
#Turn my if-else chain from Excercise 5-4 into an if-elif-else chain

#Write an if statement to test whether the alieon's color is green
def alien_color(color):
    if (color == 'green'):
    #If the alien is green, print a message that the player earned 5 points
        print("\nCongratulations! You just earned 5 points.")
    elif (color == 'yellow'):
    #If the alien is yellow, print a message that the player earned 10 points
        print("\nCongratulations! You just earned 10 points.")
    else:
    #If the alien is red, print a message that the player earned 15 points
        print("\nCongratulations! You just earned 15 points.")

#Write three versinos of the program, making sure each message is printed
#One
alien_color('green')
#The other
alien_color('yellow')
#Another
alien_color('red')