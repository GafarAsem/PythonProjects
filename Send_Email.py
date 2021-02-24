from mailer import Mailer


#creat clieant api
mail = Mailer(email='gafarasem255@gmail.com',password='gafarasem622')


#send email
mail.send(receiver='gafarasem255@gmail.com',  # Email From Any service Provider
          subject='mp3',
          message='This is th file ',
          file='')
