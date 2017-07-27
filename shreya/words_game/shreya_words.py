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
def shreya_words():

	# File containing words
	words_list_file = 'shreya_words.csv'

	# Must be between 1 and 10
	desired_word_length = 0

	# read the words from the file to this list
	words_list = []

	# store generated words to this list which will be save after the program exit
	temp_list = []

	# get the length of the words_list after getting the words from the file to this list
	words_list_length = 0	

	# read words file to a words list
	try:
		with open(words_list_file, 'r') as words_file:
			
			# get the first item from the resulting list as it contains the list of words as list
			words_list = list(csv.reader(words_file))[0]

			# Calculate the length of the words list
			words_list_length = len(words_list)

	except Exception as ex:
		print('Error reading the dictionary. ' + str(ex))

	try:
		# e.g. for 3 letters words, or 4 letters words		
		desired_word_length = int(input('Please enter number of letters in a word: '))
		
		# We are only going to generate words of minimum 1 and 14 letters
		if desired_word_length <= 0 or desired_word_length >14:
			print('Please input a number between 1 & 14.')
		else:
			# Run an infinite loop to get random words until user press other key than 'y'
			while True:

				# Loop should not run indefinitely.
				word_not_found_loop_count = 0

				# Run an inifinite loop untill a word of user's desired length of a word is found
				while True:

					# Generate a random number between 1 and the number of total words in 
					#the words list
					random_number = random.randint(1, (words_list_length-1))

					# get a random word from the list
					temp_word = words_list[random_number]

					# check if the length of the found word matches user's desired length of a word
					if(len(temp_word) == desired_word_length):

						# print the word
						print(temp_word)

						# Since word has been found. Reset the counter
						word_not_found_loop_count = 0

						# append the found word to the temp list to be saved later 
						#if it does not exist in the list
						if temp_word not in temp_list:
							temp_list.append(temp_word)

						break;

					else:
						# Increase the counter if a word is not found
						word_not_found_loop_count += 1

					# 20% of total words
					# Break the loop and exit the program if a word is not found after 300 iteration
					if word_not_found_loop_count > 1000:
						print('Sorry! No more words of ' + str(desired_word_length) + ' characters long are not available.')
						
						# Save exercise file and exit
						save_exercise_file(temp_list)
						sys.exit()
						break;

				# Check if the user wants to continue running the program by inputting 'y' key
				# Save found words to exercise file and exit if the user does not want to continue 
				#running the program
				if(str(input('Input \'y\' to continue or press any key to exit: ')).upper() != 'Y'):

					# Save exercise file and exit
					save_exercise_file(temp_list)
					break;
			
	except ValueError as ve:
		print('Please input a number between 1 and 10')

	except OSError as ose:
		print('Exercise File could not be created')

	except Exception as ex:
		print(random_number)
		print('Error: ' + str(ex))

def save_exercise_file(temp_list):
	try:
		# Get dir path where this file is residing
		current_dir = str(os.path.dirname(os.path.abspath(__file__)))

		# timestamped exercise file
		new_file_name = current_dir + '/exercises/'+str(datetime.datetime.now()) + '.txt'

		# if exercises directory is not available then create
		if not os.path.exists(os.path.dirname(new_file_name)):
			os.makedirs(os.path.dirname(new_file_name))

		# Save all the found words in the exercise file
		with open(new_file_name, 'w') as temp_file:
			csv_writer = csv.writer(temp_file)
			csv_writer.writerow(temp_list)
	except OSError as ose:
		print('Exercise File could not be created')

	except Exception as ex:		
		print('Error: ' + str(ex))
	

shreya_words()