import random, datetime, csv, sys

'''
read original list of words
ask for length of a word. ex 3 letter words
get a random word from the words list
save the generated word to a temporary list
ask for confirmation to continue
when negative confirmation save the temporary list to a file based on timestamp and exit
'''
def wordslist():
	words_list_file = 'shreya_words.csv'	#
	desired_word_length = 0	# Must be between 1 and 10
	words_list = []	# read the words from the file to this list
	temp_list = []	# store generated words to this list which will be save after the program exit
	words_list_length = 0	# get the length of the words_list after getting the words from the file to this list


	# read words file to a words list
	try:
		with open(words_list_file, 'r') as words_file:
			# get the first item from the resulting list as it contains the list of words as list
			words_list = list(csv.reader(words_file))[0]
			# Calculate the length of the words list
			words_list_length = len(words_list)
	except Exception as ex:
		print('Error reading the dictionary. ' + str(ex))
	
	#print('words list length: ' + str(len(words_list)))	

	try:
		# e.g. for 3 letters words, or 4 letters words
		print('Please enter number of letters in a word', end=': ')	
		desired_word_length = int(input())
		
		# We are only going to generate words of minimum 1 and 10 letters
		if desired_word_length <= 0 or desired_word_length >10:
			print('Please input a number between 1 & 10.')
		else:
			while True:
				# Run an inifinite loop untill a word is found
				while True:
					# Generate a random number between 1 and the number of total words in the words list
					random_number = random.randint(1, words_list_length)
					# get a random word from the list
					temp_word = words_list[random_number]
					# if the length of the found word matches desired length then 					
					if(len(temp_word) == desired_word_length):
						# print the word
						print(temp_word)
						# and append to the temp list
						temp_list.append(temp_word)
						break;

				print('Input \'y\' to continue or press any key to exit ', end=': ')
				if(str(input()).upper() == 'Y'):
					pass
				else:
					new_file_name = str(datetime.datetime.now()) + '.txt'
					with open(new_file_name, 'w') as temp_file:
						csv_writer = csv.writer(temp_file)
						csv_writer.writerow(temp_list)
					break;
			
	except ValueError as ve:
		print('Please input a number between 1 and 10')
	except Exception as ex:
		print('Error: ' + str(ex))

wordslist()