import csv

'''
purpose of this file is to create a csv file from a text file
'''


words_list = []

with open('shreya_words.txt', 'r') as words_file:
	csv_list = list(csv.reader(words_file))

for words in csv_list:
	for word in words:
		words_list.append(word)

with open('shreya_words.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
	csv_writer.writerow(words_list)

print(words_list)
