import csv

with open("data.csv", "w+") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["col 1", "col 2"])
	writer.writerow(["data 1", "data 2"])

with open("data.csv", "r") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)

with open("data.csv", "a") as csvfile:
	writer = csv.writer(csvfile)	
	writer.writerow(["data 3", "data 4"])
	
with open("data.csv", "r") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)

with open("data.csv", "a") as csvfile:
	fieldnames = ["id", "title"]	
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({"id":123, "title": "New Title"})