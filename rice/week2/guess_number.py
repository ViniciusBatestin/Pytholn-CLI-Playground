# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
'''
Simple gui module does not exist outside of codeSkulptor
'''
import simplegui
import math
import random

# Global variables
secret_number = 0
allowed_guesses = 0
current_mode = 1

# helper function to start and restart the game
def new_game(mode=1):
    # initialize global variables used in your code here
    global secret_number, allowed_guesses, current_mode
    current_mode = mode

    if mode == 1:
        low = 0
        high = 100
        secret_number = random.randrange(low,high)
        # print secret_number (debbug)
    elif mode == 2:
        low = 0
        high = 1000
        secret_number = random.randrange(low,high)
        # print secret_number (debbug)

    allowed_guesses = math.ceil(math.log(high - low + 1, 2))
    print("A NEW GAME JUST START")
    print ("")
    print ("You have " + str(allowed_guesses) + " ramaining guesses!")
    print ("")


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    print ('Range from 0 - 100')
    new_game(1)

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    print('Range from 0 - 1000')
    new_game(2)

def input_guess(guess):
    global secret_number, allowed_guesses
    guess_number = int(guess)
    print ("Guess was " + guess)

    allowed_guesses -= 1
    print("Number of remaining guesses are: " + str(allowed_guesses))
    # main game logic goes here

    if allowed_guesses == 0 and guess_number != secret_number:
        print ("You run out of guesses")
        new_game(current_mode)
    elif guess_number > secret_number:
        print ("Lower")
    elif guess_number < secret_number:
        print("Higher")
    else:
        print ("Correct")
        print("")
        new_game()





# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
input = frame.add_input('My Guess', input_guess, 100)
range100 = frame.add_button('Range is [0,100)', range100, 100)
range1000 = frame.add_button('Range is [0,1000)', range1000, 100)

# call new_game
new_game()


# always remember to check your completed program against the grading rubric


'''
1 - I start with  ** n >= high - low + 1 amount of chances. depending on the range
0 - 100 = 7 chances
0 - 10000 = 10 chances

add it in the function new_game()
set the number of allowed guess to seven when the range is
[0, 100)
[0, 100) or to ten when the range is
[0, 1000)
[0, 1000).

For more of a challenge, you may compute n from low and high
using the function math.log and match ceil in the match module


'''
