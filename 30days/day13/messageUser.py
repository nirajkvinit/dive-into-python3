import datetime
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "nirajkvinit@gmail.com"
password = input("Please enter your password: ")

from_email = username
to_list = ["nirajkvinit@yahoo.co.in"]

class MessageUser():
	user_details = []
	email_messages = []
	messages = []
	base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""
	def add_user(self, name, amount, email = None):
		name = name[0].upper() + name[1:].lower()
		amount = "%.2f" %(amount)
		detail = {
			"name" : name,
			"amount" : amount,
		}
		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		detail['date'] = date_text

		if email is not None:
			detail["email"] = email
		self.user_details.append(detail)

	def get_details(self):
		return self.user_details

	def make_messages(self):
		if len(self.user_details) > 0:
			for detail in self.get_details():
				name = detail["name"]
				amount = detail["amount"]
				date = detail["date"]
				message = self.base_message
				new_msg = message.format(
					name = name,
					date = date,
					total = amount
				)
				user_email = detail.get("email")
				if user_email:
					user_data = {
						"email" : user_email,
						"message" : new_msg
					}
					self.email_messages.append(user_data)
				else:
					self.messages.append(new_msg)
			return self.messages
		else:
			return []
	def send_email(self):
		self.make_messages()
		if len(self.email_messages) > 0:
			if len(password) > 0:
				try:
					email_conn = SMTP(host, port)
					email_conn.ehlo()
					email_conn.starttls()
					email_conn.login(username, password)
				except SMTPAuthenticationError as authError:
					print("Email authentication error! {0}".format(authError))					
					return False
				except Exception as e:
					print("Sorry! Email Connection error. An error occured. {0}".format(e))
					return False

				for detail in self.email_messages:
					user_email = detail['email']
					user_message = detail['message']
					# run email here
					try:
						the_msg = MIMEMultipart("alternative")
						the_msg['Subject'] = "Billing Update"
						the_msg['From'] = from_email
						the_msg['To'] = user_email
						part1 = MIMEText(user_message, 'plain')
						the_msg.attach(part1)
						email_conn.sendmail(from_email, [user_email], the_msg.as_string() )
						print("Email to {0} sent successfully!".format(user_email))
					except Exception as e:
						print("Sorry! Email could not be sent. An error occured. {0}".format(e))					
				return True
		return False

obj = MessageUser()
obj.add_user("Niraj", 123.32, "nirajkvinit@yahoo.co.in")
obj.add_user("john", 94.23, "nirajkvinit@gmail.com")
obj.add_user("Emilee", 124.32, "mail@novamining.com")
#print(obj.make_messages())
obj.send_email()

