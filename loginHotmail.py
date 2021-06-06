import email
import smtplib



s = smtplib.SMTP("smtp.live.com",587)
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login('example@hotmail.com', '12445qwert')


print('done')
s.quit()
