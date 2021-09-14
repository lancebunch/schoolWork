# 1. Name: 
#    Lance Bunch
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This is a simple game that lets you guess a number, keeps track of guesses, and the
#    Values of those guesses.
# 4. What was the hardest part? Be as specific as possible.
#    The easiest part of the assignment was the logic. Very simple game that loops until
#    the correct guess was made. What started out a psuedocode turned immedietely into
#    a real algorithm very quickly.
#    While I haven't worked with Python in abuot 4 years, for me what has been the most
#    difficult part are the print statements and what are allowed in them as well as
#    dealing with variable type comparisons. I haven't been able to find a way to accept
#    input as a certain data type such as 'int' or 'str'. It automatically makes any input
#    a string which means I had to typecast any input that I wanted to be an integer
#    evertime I wanted to use that input. There has got to be an easier way.
#    The other part was dealing with print statements. I'm still not sure how to manipulate 
#    them fully but I figured them out enough to print all the required information.
# 5. How long did it take for you to complete the assignment?
#    It took about 3 hours to study the assignment, research, code, and test. 

import random

# Game introduction
print('This is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts.\n')

# Prompt the user for how difficult the game will be. Ask for an integer
value_max = input('Pick a positive integer: ')

# Generate a random number between 1 and the chosen value
value_random = random.randint(1, int(value_max))

# Give the user instructions as to what he or she will be doing
print('Guess a number between 1 and %s.' % value_max)

# Initialize the sentinal and the array of guesses
guessList = []
myGuess = 0
numGuesses = 0

# Play the guessing game
while myGuess != value_random:

    # Prompt the user for a number
    myGuess = input('> ')

    # Store the number in an array so it can be displayed later
    guessList.append(myGuess)
    numGuesses += 1

    # Make a decision: was the guess too high, too low, or just right
    if int(myGuess) > value_random:
        print('\tToo high!')
        pass
    elif int(myGuess) < value_random:
        print('\tToo low!')
        pass
    else:
        break

# Give the user a report: How many guesses and what the guesses where
print('You were able to find the number in %d guesses.' % numGuesses)
print('The numbers you guessed were: ', guessList)

