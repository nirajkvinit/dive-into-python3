from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
username = "apple@gmail.com"
password = input("Please enter your password: ")
from_email = username
to_list = ["email@example.com"]
email_sent = True
if len(password) > 0:	
	email_conn = SMTP(host, port)
	email_conn.ehlo()
	print("Please wait... Connecting to the SMTP Server and trying to send your email.")
	email_conn.starttls()
	try:
		email_conn.login(username, password)
		email_conn.sendmail(from_email, to_list, "This is a test email sent from a pythong module")
	except SMTPAuthenticationError as authError:
		print("Email authentication error! {0}".format(authError))
		email_sent = False
	except Exception as e:
		print("Sorry! Email could not be sent. An error occured. {0}".format(e))
		email_sent = False
	email_conn.quit()
	if email_sent:
		print("Email was sent successfully!")
