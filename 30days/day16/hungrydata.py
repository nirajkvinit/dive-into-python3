import csv
import shutil
from tempfile import NamedTemporaryFile
import datetime

def get_length(file_path):
	with open("data.csv") as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
	return len(reader_list)

def append_data(file_path, name, email, amount):
	fieldnames = ["id", "name", "email", "amount", "sent", "date"]
	next_id = get_length(file_path)

	with open(file_path, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		#writer.writeheader()
		writer.writerow({
			"id": next_id,
			"name": name,
			"email": email,
			"amount": amount,
			"sent": "",
			"date": datetime.datetime.now(),
		})

#append_data("data.csv", "Niraj", "nirajkvinit@gmail.com", 123.45)

def edit_data(edit_id=None, email=None, amount=None, sent=None):
	file_name = "data.csv"
	temp_file = NamedTemporaryFile(delete=False)

	with open(file_name, 'r') as csvfile:

		fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']

		reader = csv.DictReader(csvfile)

		with open("temp.csv", 'w') as temp_file:
			writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
			writer.writeheader()

			for row in reader:
				if edit_id is not None:
					if int(row['id']) == int(edit_id):
						row['amount'] = amount
						row['sent'] = sent
				elif email is not None and edit_id is None:
					if str(row['email']) == str(email):
						row['amount'] = amount
						row['sent'] = sent
				else:
					pass
				writer.writerow(row)

			shutil.move(temp_file.name, file_name)
			return True
	return False
	
edit_data(email='nirajkvinit@gmail.com', amount=90.99, sent=True)	