# Import text files as lists

# Startup Message

# Outer Game Loop

    # Ask player for length of word to play

    # Choose a word at random from the appropriate list - choice

    # Allow one more guess than the length of the word
    won = False

    # Main Game Loop
        # for wordlength +1 times
            # Get the user's guess
        # create a list, status, the length of the word, with each index representing the guess status
        # set each item in the list to 0
        # calculate score for the guess - checkWord func
        # print the guess - printWord func
        # if user guessed exactly right, set won var to true, and break

    # Print the game's result

    # Ask user if they want to play again or quit






# FUNCTIONS
def getGuess (wordlength)
'''
Accepts the length of the word, an int
Prompts the user to type their answer, and only accepts the correct-length word
RETURNS: the user's guess, a string
'''


def checkWord(guess, wordsize, status, choice)
'''
Compares the user's guess to the choice word and scores points as appropriate
Stores points in status
If a letter in guess is in the same position as choice, score 2 points
In addition to scoring a point, updates the corresponding letter space in status to a 2
Elif a letter in guess is in choice but not in the same position, score 1 point
In addition to scoring a point, updates the corresponding letter space in status to a 1
RETURNS: score, an int
'''


def printWord(guess, wordsize, status)
'''
print word character for character with correct color coding
'''
# RESEARCH HOW TO PRINT COLOR