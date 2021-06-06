import smtplib
from mailer import Mailer
from mailer import Message

gmail_user = 'gafarasem255@gmail.com'
gmail_password = '@zz00z255'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail('gafarasem255@gmail.com', 'susn622@gmail.com', "ssssss")
server.close()
