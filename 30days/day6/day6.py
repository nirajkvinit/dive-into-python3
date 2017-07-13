import datetime
default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

default_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

def make_messages(names, amounts):
	messages = []
	if len(names) == len(amounts):
		i = 0
		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		for name in names:
			new_amount = "%.2f" %(amounts[i])
			new_msg = default_message.format(
					name = name.title(),
					date = date_text,
					total = new_amount
				)
			i += 1
			print(new_msg)

make_messages(default_names, default_amounts)
