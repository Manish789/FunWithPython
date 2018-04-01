import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = '''apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'''.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings. 
    wordIndex = random.randint(0,len(wordList) -1 )
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Lettes: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_'* len(secretWord)
    # Replace blanks with correctly guessed letters.
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # Show the secret word with spaces in between each letter.
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
	# Returns the letter the player entered. This function makes sure the player
	# entered  a single letter and not something else
	while True:
		print("Guess a letter.")
		guess =input()
		guess = guess.lower()
		if len(guess) != 1:
			print("Please enter a single letter.")
		elif guess in alreadyGuessed:
			print("You have already guessed that letter. Choose again. ")
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print("Please enter a LETTER.")
		else:
			return guess

def playAgain():
	# This function returns True if the player wants to play again; otherwise, it returns False.
	print("Do you want to play again ? (yes or no)")
	return input().lower().startswith('y')
	
print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameisDone = False

while True:
	displayBoard(missedLetters, correctLetters, secretWord)
	
	# Let the player enter a letter
	guess = getGuess(missedLetters+correctLetters)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		
		# Check if the player has won.
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print("Yes! The secret word is " + secretWord + "! You have won!")
			gameisDone = True
	else:
		missedLetters = missedLetters + guess
		
		# Check if player has guessed too many times and lost.
		if len(missedLetters) == len(HANGMAN_PICS) -1:
			displayBoard(missedLetters,correctLetters,secretWord)
			print("You have run out of guesses!\n After " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses, the word was " + secretWord)
			gameisDone = True
			
	# Ask the player if they want to play again(but only if the game is done. )
	if gameisDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameisDone = False
			secretWord = getRandomWord(words)
		else:
			break
