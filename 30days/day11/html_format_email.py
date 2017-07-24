from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "nirajkvinit@gmail.com"
password = input("Please enter your password: ")

from_email = username
to_list = ["nirajkvinit@yahoo.co.in"]

email_sent = True

if len(password) > 0:	
	email_conn = SMTP(host, port)
	email_conn.ehlo()
	print("Please wait... Connecting to the SMTP Server and trying to send your email.")
	email_conn.starttls()

	try:
		email_conn.login(username, password)
		
		the_msg = MIMEMultipart("alternative")
		the_msg['Subject'] = "Hello there!"
		the_msg['From'] = from_email
		#the_msg['To'] = to_list[0]
		
		plain_txt = "Testing the message"
		
		html_text = """ 
			<html>
				<head></head>
				<body>
					<p>Hey! <br>
						This this email <strong>Message</strong>. Made by <strong>Niraj</strong>.
					</p>
				</body>
			</html>
		"""
		part1 = MIMEText(plain_txt, 'plain')
		part2 = MIMEText(html_text, 'html')
		
		the_msg.attach(part1)
		the_msg.attach(part2)

		email_conn.sendmail(from_email, to_list, the_msg.as_string() )
	except SMTPAuthenticationError as authError:
		print("Email authentication error! {0}".format(authError))
		email_sent = False
	except Exception as e:
		print("Sorry! Email could not be sent. An error occured. {0}".format(e))
		email_sent = False
	finally:
		email_conn.quit()
		
	if email_sent:
		print("Email was sent successfully!")
