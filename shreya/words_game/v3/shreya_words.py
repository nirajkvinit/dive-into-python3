import random, datetime, csv, os, sys, platform, colorama

'''
read original list of words
ask for length of a word. ex 3 letter words
get a random word from the words list
save the generated word to a temporary list
ask for confirmation to continue
when negative confirmation save the temporary list to a file based on timestamp and exit

@author : nirajkvinit@yahoo.co.in
'''

# Clears the screen
def clearScreen():	
	command = "-cls" if platform.system().lower()=="windows" else "clear"
	os.system(command)

def getWordsList(wordsFile = None):
	
	# File containing words
	wordsListFile = 'wordslist.csv'

	# Words List to be returned
	wordsList = None

	# if wordsFile is not provided then use the default one
	if wordsFile is None:
		wordsFile = wordsListFile
	# read words file to a words list
	try:
		with open(wordsFile, 'r') as csvFile:
			
			# get the first item from the resulting list as it contains the list of words as list
			wordsList = list(csv.reader(csvFile))[0]			

	except Exception as ex:
		print('Error reading the dictionary. ' + str(ex))

	return wordsList


def getRandomWord(wordsList):

	foundWord = None

	if wordsList is not None:
		# get the length of the wordsList after getting the words from the file to this list
		wordsListLength = len(wordsList)

		# Generate a random number between 1 and the number of total words in 
		#the words list
		randomNumber = random.randint(1, (wordsListLength - 1))

		# get a random word from the list
		foundWord = wordsList[randomNumber]

	return foundWord

def shreyaWordsGame(wordsList):
	if wordsList is None:
		print('Error! Words list not available! Exiting the game!')
		sys.exit()

	while True:	
		
		clearScreen()
		print(colorama.Fore.WHITE + colorama.Back.GREEN + 'Welcome to Shreya\'s Words Game!')
		print(colorama.Style.RESET_ALL)

		print('Please select your Game: ')
		# Random Words
		print('1. Random words.')
		# Random words where the word begins with a desired letter
		print('2. Random words of your desired first letter.')
		# Random words of desired length
		print('3. Random words of your desired word length.')

		print(colorama.Fore.WHITE + colorama.Back.RED + 'Press \'q\' to exit the game.')
		print(colorama.Style.RESET_ALL)

		gameChoice = str(input('Please input your choice: ')).strip().lower()

		if gameChoice == 'q':
			break;

		elif gameChoice == '1':
			shreyaRandomWords(wordsList)

		elif gameChoice == '2':
			pass

		elif gameChoice == '3':
			pass

		else:
			input('Your input was incorrect! Press \'Enter\' key to try again!')

		input()	# Allow to press enter before screen clears out
	clearScreen()
	print(colorama.Fore.WHITE + colorama.Back.MAGENTA + 'Thank you for playing Shreya\'s Game! Goodbye!')
	print(colorama.Style.RESET_ALL)


def shreyaRandomWords(wordsList):
	while True:
		clearScreen()
		print(colorama.Fore.WHITE + colorama.Back.CYAN + 'Random Words Game!')
		print(colorama.Style.RESET_ALL)
		print('\n' * 3)
		print('{0: ^20}'.format(getRandomWord(wordsList)))		
		print('\n' * 3)
		gameChoice = str(input(colorama.Fore.WHITE + colorama.Back.RED + 'Press \'Enter\' to continue or \'q\' to exit the game: ')).lower()
		print(colorama.Style.RESET_ALL)

		if gameChoice == 'q':
			break;

def saveExerciseFile(exerciseWordsList):
	try:
		# Get dir path where this file is residing
		currentDir = str(os.path.dirname(os.path.abspath(__file__)))

		# timestamped exercise file
		newFileName = currentDir + '/exercises/'+str(datetime.datetime.now()) + '.txt'

		# if exercises directory is not available then create
		if not os.path.exists(os.path.dirname(newFileName)):
			os.makedirs(os.path.dirname(newFileName))

		# Save all the found words in the exercise file
		with open(newFileName, 'w') as exerciseFile:
			csvWriter = csv.writer(exerciseFile)
			csvWriter.writerow(exerciseWordsList)

	except OSError as ose:
		print('Exercise File could not be created.' + str(ose))

	except Exception as ex:		
		print('Error: ' + str(ex))
	

#shreyaWords(wordsList())
shreyaWordsGame(getWordsList())