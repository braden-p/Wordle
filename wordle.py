

import random

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
        guess = input().lower()
        if len(guess) == wordlength and guess.isalpha():
            validGuess = True
        elif len(guess) != wordlength:
            print('Please enter a word with exactly', wordlength, 'letters.')
        else:
            print('Please enter only letters.')
    return guess
        

def checkWord(guess, status, choice):
    '''
    Compares the user's guess to the choice word and scores points as appropriate
    Stores points in status
    If a letter in guess is in the same position as choice, score 2 points
    In addition to scoring a point, updates the corresponding letter space in status to a 2
    Elif a letter in guess is in choice but not in the same position, score 1 point
    In addition to scoring a point, updates the corresponding letter space in status to a 1
    RETURNS: score, an int
    '''
    score = 0
    guessIndex = 0
    for letter in guess:
        choiceIndex = 0
        for letter in choice:
            if guess[guessIndex] == choice[guessIndex]:
                status[guessIndex] = 2
                break
            elif guess[guessIndex] == choice[choiceIndex]:
                status[guessIndex] = 1
            choiceIndex += 1
        guessIndex += 1
    score = sum(status)
    return score

def colorText(character, colorCode):
    '''
    Accepts a character, and a colorCode (an int)
    Prints the character with the corresponding colorCode background
    valid colorCodes: 0 = Red, 1 = Yellow, 2 = Green
    Resets background color to normal
    '''
    if colorCode == 0:
        print('\u001b[41m' + character + '\u001b[0m', end = '')
    elif colorCode == 1:
        print('\u001b[43;1m' + character + '\u001b[0m', end = '')
    else:
        print('\u001b[42;1m' + character + '\u001b[0m', end = '')


def printWord(guess, status):
    '''
    print word character for character with correct color coding
    '''
    index = 0
    for colorCode in status:
        colorText(guess[index], colorCode)
        index += 1
    print('')


def print_alphabet(guess, status, guesses):
    # Add the current guess and status to the list of guesses
    guesses.append((guess, status))
    
    # Create a set of all the letters that have been guessed
    guessed_letters = set([g[0][i] for g in guesses for i in range(len(g[0]))])
    
    # Create a list of letters with their corresponding color
    letters = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in guessed_letters:
            # Letter not guessed yet
            letters.append((letter, None))
        else:
            # Letter guessed
            found = False
            for g in guesses:
                if letter in g[0]:
                    if g[1][g[0].index(letter)] == 2:
                        # Letter in correct position
                        letters.append((letter, 'green'))
                        found = True
                        break
                    elif g[1][g[0].index(letter)] == 1:
                        # Letter in wrong position
                        letters.append((letter, 'yellow'))
                        found = True
                        break
            if not found:
                # Letter not in word
                letters.append((letter, 'red'))
    
    # Print the alphabet with the appropriate colors
    for letter, color in letters:
        if color is None:
            print(letter, end=' ')
        elif color == 'red':
            #print(f"\033[91m{letter}\033[0m", end=' ')
            print('\u001b[41m' + letter + '\u001b[0m', end = ' ')
        elif color == 'yellow':
            #print(f"\033[93m{letter}\033[0m", end=' ')
            print('\u001b[43;1m' + letter + '\u001b[0m', end = ' ')
        elif color == 'green':
            #print(f"\033[92m{letter}\033[0m", end=' ')
            print('\u001b[42;1m' + letter + '\u001b[0m', end = ' ')
    print()


# Startup Message
print("Welcome to Wordle.")

# Ask player for length of word to play
wordlength = 0
while wordlength != 5 or 6 or 7 or 8:
    wordlength = int(input('What length word would you like to play; 5, 6, 7, or 8 letters? '))
    # Choose a word at random from the appropriate list = choice
    if wordlength == 5:
        choice = random.choice(wordslist5)
        break
    elif wordlength == 6:
        choice = random.choice(wordslist6)
        break
    elif wordlength == 7:
        choice = random.choice(wordslist7)
        break
    elif wordlength == 8:
        choice = random.choice(wordslist8)
        break
    else:
        print('Invalid input. Please type 5, 6, 7, or 8.')

# Allow one more guess than the length of the word
guesses = wordlength + 1
won = False
prevGuesses = []
# Main Game Loop
for numGuesses in range(guesses):
    print(guesses, 'guesses left.')
    # Get the user's guess
    guess = getGuess(wordlength)
    status = []
    for letter in range(wordlength):
        status.append(0)
    score = checkWord(guess, status, choice)
    printWord(guess, status)
    print_alphabet(guess, status, prevGuesses)
    guesses -= 1
    # if user guessed exactly right, set won var to true, and break
    if score == (2 * wordlength):
        won = True
        break

# Print the game's result
if won == True:
    print('You won!')
else:
    print('Better luck next time. The word was', choice)


# TODO
# Implement replayability