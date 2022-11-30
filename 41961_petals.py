# Place ALL import statements at the top of your file
import dice
import random

# File: 41961_petals.py <-- Replace with *your* file name
# Author: Thanh Son Aiden Nguyen <-- Replace with *your* name
# Email Id: nguty385@mymail.unisa.edu.au <-- Replace with *your* email id
# Description: Assignment 1 - Part 1 of assignment 1 / Roses and petals
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
#

#Function for my deatils
def display_details():
    print("File: 41961_petals.py")
    print("Author: Thanh Son Aiden Nguyen")
    print("Stud ID: 41961")
    print("Email ID: nguty385")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")



#Variable to store where the user wants to play or not
play = "y"
#List to aid in validating user input
valid = ["y","n"]
#List to help iterate through the casted die
list = []
#The very many variables to store the die rolls, i hate looking at it. It's so not elegant.
die1 = 0
die2 = 420
die3 = 7336
die4 = 203
die5 = -1
#Variable to store the number of petals around the rose
petals = 0
#Variable to store the user's guess of how many petals are on the roses
guess = 0
#Variables to store the user's win/loss streak
winstreak = 0
loststreak = 0
#Variables to store the total number of wins/losses
wins = 0
losts = 0
#Variable to determine whether the player wants to quit after finishing a round of the game
quit = False
#Variable to check if the user entered a valid character while guessing
check = True
#Variable to skip the first input asking the user to punch in y/n
skip = 0


display_details()
print("")
print("Petals Around The Rose")
print("----------------------")
print("The name of the game is 'Petals Around The Rose'. The name of the")
print("game is important. The computer will roll five dice and ask you to")
print("guess the score for the roll. The score will always be zero or an")
print("even number. Your mission, should you choose to accept it, is to")
print("work out how the computer calculates the score. If you succeed in")
print("working out the secret and guess correctly four times in a row, you")
print("become a Potentate of the Rose.")
print("")
#I'm sure there was a more eloquent way to print out this prompt but oh well

while play == "y":
    if skip == 0:
        play = input("Would you like to play Petals Around The Rose [y|n]? ")
        skip += 1
        while play not in valid:
            play = input("Would you like to play Petals Around The Rose [y|n]? ")
    #this while loop is here to prevent any 'n' inputs from starting the game and instead exiting the while loop
    while play == "y":
        (die1,die2,die3,die4,die5) = (random.randint(1,6) for x in range(5))
        #I used i to iterate through dierolls because well... 'i' for iterate hehe
        list = (die1,die2,die3,die4,die5)
        for i in list:
            if i == 3:
                petals += 2
            elif i == 5:
                petals += 4
            else:
                petals += 0

        dice.display_dice(die1,die2,die3,die4,die5)

        guess = input("The die have been cast, please enter your guess for the roll: ")
        while check:
            #The wins/losts variables will incease by one if the user wins or loses respectively. If the user wins the losses reset to 0 and vice versa.
            #The check variable is here for the purpose of validating user input while guessing
            if guess.isdigit():
                if int(guess) == petals:
                    print("Well done! You guessed it!")
                    winstreak += 1
                    wins += 1
                    loststreak = 0
                    check = False
                elif (int(guess) % 2) != 0:
                    print("No sorry, it's",petals,"not",str(guess) + ".","The score is always even.")
                    loststreak += 1
                    winstreak = 0
                    losts += 1
                    check = False
                elif (int(guess) % 2) == 0:
                    print("No sorry, it's",petals,"not",str(guess) + ".")
                    loststreak += 1
                    winstreak = 0
                    losts += 1
                    check = False
            else:
                guess = input("Please enter your answer as an integer: ")

        #This next sequence of code is to see whether the player has reached a 4 game win or loss streak and to act on it if so.
        if winstreak >= 4:
            print("Congratulations! You have worked out the secret!")
            print("Make sure you don't tell anyone!")
            play = input("Roll dice again [y|n]? ")
            if play == "n":
                play = False
                quit = True
            elif play == "y":
                print("Here we go again!")
        #Reverting the 'die5' value back to -1 to prompt another series of dice to be cast
                die5 = -1
                petals = 0
        #Reverting check back to True after the input validation allows for the validation to occur again if the user wants to play again
                check = True
            else:
                play = input("Would you like to play Petals Around The Rose [y|n]? ")

        elif loststreak >= 4:
            print("Hint the name of the game is important... Petals around the rose.")
            play = input("Roll dice again [y|n]? ")
            if play == "n":
                play = False
                quit = True               
            elif play == "y":
                print("Here we go again!")
                die5 = -1
                petals = 0
                check = True
            else:
                play = input("Would you like to play Petals Around The Rose [y|n]? ")

        else:
            play = input("Roll dice again [y|n]? ")
            if play == "n":
                play = False
                quit = True
            elif play == "y":
                print("Here we go again!")
                die5 = -1
                petals = 0
                check = True
            else:
                play = input("Would you like to play Petals Around The Rose [y|n]? ")

#the quit variable is here to determine which exit scene to play. The "no worries" or the game summary.
if play == "n" and quit == 0:
    print("")
    print("No worries... another time perhaps... :)")

if quit == True:
    print("Game Summary")
    print("============")
    print("")
#I was thinking "should i add ANOTHER variable to see how many times they played?"" Then i got lazy and figured this is work. I think this might be better actually...
    print("You played", wins + losts, "games:")
    print(" Number of correct guesses:", wins)
    print(" Number of incorrect guesses:", losts)

