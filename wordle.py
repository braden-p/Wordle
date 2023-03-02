# Import text files as lists
file_5 = open('5.txt', 'r')
words5 = file_5.read()
wordslist5 = words5.split('\n')
file_5.close()

file_6 = open('6.txt', 'r')
words6 = file_6.read()
wordslist6 = words6.split('\n')
file_6.close()

file_7 = open('7.txt', 'r')
words7 = file_7.read()
wordslist7 = words7.split('\n')
file_7.close()

file_8 = open('8.txt', 'r')
words8 = file_8.read()
wordslist8 = words8.split('\n')
file_8.close()

# FUNCTIONS
def getGuess (wordlength):
    '''
    Accepts the length of the word, an int
    Prompts the user to type their answer, and only accepts the correct-length word
    RETURNS: the user's guess, a string
    '''
    validGuess = False
    while validGuess == False:
        print('Type a', wordlength, 'letter word.')
        guess = input()
        if len(guess) == wordlength:
            validGuess = True
        else:
            print('Please enter a word with exactly', wordlength, 'letters.')
    return guess
        


def checkWord(guess, wordsize, status, choice):
    '''
    Compares the user's guess to the choice word and scores points as appropriate
    Stores points in status
    If a letter in guess is in the same position as choice, score 2 points
    In addition to scoring a point, updates the corresponding letter space in status to a 2
    Elif a letter in guess is in choice but not in the same position, score 1 point
    In addition to scoring a point, updates the corresponding letter space in status to a 1
    RETURNS: score, an int
    '''


def printWord(guess, wordsize, status):
    '''
    print word character for character with correct color coding
    '''

# Startup Message
print("Welcome to Wordle.")
# Outer Game Loop

    # Ask player for length of word to play
wordlength = input('What length word would you like to play, 5, 6, 7, or 8 letters?')

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









# RESEARCH HOW TO PRINT COLOR