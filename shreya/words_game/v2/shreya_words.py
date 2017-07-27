import random, datetime, csv, os, sys

'''
read original list of words
ask for length of a word. ex 3 letter words
get a random word from the words list
save the generated word to a temporary list
ask for confirmation to continue
when negative confirmation save the temporary list to a file based on timestamp and exit

@author : nirajkvinit@yahoo.co.in
'''

def wordsList(wordsFile = None):
	
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


def shreyaWords(wordsList):
	# Must be between 1 and 10
	desiredWordLength = 0

	# read the words from the file to this list
	#wordsList = wordsList()

	# store generated words to this list which will be save after  t he program exit
	exerciseWordsList = []

	if wordsList is None:
		print('Sorry! Words List is not available!')

	# get the length of the wordsList after getting the words from the file to this list
	wordsListLength = len(wordsList)

	try:
		# e.g. for 3 letters words, or 4 letters words		
		desiredWordLength = int(input('Please enter the length of a word: '))
		
		# We are only going to generate words of minimum 1 and 14 letters
		if desiredWordLength <= 0 or desiredWordLength >14:
			
			print('Please input a number between 1 & 14.')

		else:

			# Run an infinite loop to get random words until user press other key than 'y'
			while True:

				# Loop should not run indefinitely.
				wordNotFoundLoopCount = 0

				# Run an inifinite loop untill a word of user's desired length of a word is found
				while True:

					# Generate a random number between 1 and the number of total words in 
					#the words list
					randomNumber = random.randint(1, (wordsListLength - 1))

					# get a random word from the list
					foundWord = wordsList[randomNumber]

					# check if the length of the found word matches user's desired length of a word
					if(len(foundWord) == desiredWordLength):

						# print the word
						print(foundWord)

						# Since word has been found. Reset the counter
						wordNotFoundLoopCount = 0

						# append the found word to the temp list to be saved later 
						#if it does not exist in the list
						if foundWord not in exerciseWordsList:
							exerciseWordsList.append(foundWord)

						# Since word has been found of desired length break out of the loop
						break;

					else:
						# Increase the counter if a word is not found
						wordNotFoundLoopCount += 1

					# 30% of total words
					# Break the loop and exit the program if a word is not found after 1000 iteration
					if wordNotFoundLoopCount > 1000:
						print('Sorry! No more words of ' + str(desiredWordLength) + ' characters long are not available.')
						
						# Save exercise file and exit
						saveExerciseFile(exerciseWordsList)
						sys.exit()

						# will never reach here
						break;

				# Check if the user wants to continue running the program by inputting 'y' key
				# Save found words to exercise file and exit if the user does not want to continue 
				#running the program
				if(str(input('Input \'y\' to continue or press any key to exit: ')).upper() != 'Y'):

					# Save exercise file and exit
					saveExerciseFile(exerciseWordsList)
					break;
			
	except ValueError as ve:
		print('Please input a number between 1 and 10')

	except OSError as ose:
		print('Exercise File could not be created')

	except Exception as ex:
		print(randomNumber)
		print('Error: ' + str(ex))

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
	

shreyaWords(wordsList())