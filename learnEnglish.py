from googletrans import*
import googletrans
import random
from gtts import gTTS
import os
from twilio.rest import Client
from mailer import Mailer
import telegram

user=input("Enter user id : ")
def send():
    path="D:/Dell/Desktop/Codes/"+text_+".mp3"
    bot = telegram.Bot(token='1337789917:AAE9ud2Xhck9VQYfKqDk-GzTFHaqWG30N2s')
    bot.sendMessage(chat_id=user, text=text_+"  \n"+result.text)
    bot.send_audio(chat_id=user, audio=open(path, 'rb'))
    os.remove(path)
sentences=[
 "Believe me",
 "Call me back",
 "As soon as possible" ,
 "Give me a hand" ,
 "I do not understand" ,
 "I do not mean it" ,
 "How much is it" ,
 "How old are you" ,
 "How was your weekend" ,
 "What did you say" ,
 "What do you need" ,
 "What do you think" ,
 "What do you want to do" ,
 "What do you want" ,
 "What's the weather like" ,
 "Where are you going" ,
 "It's Ok" ,
 "It really takes time" ,
 "It's fort he best" ,
 "No, I don't want" ,
 "See you later" ,
 "See you next time" ,
 "So I do ",
 "I decline ",
 "What's your e-mail ",
 "address ",
 "What is your job ",
 "What's your name ",
 "What's your phone ",
 "number ",
 "What is going on ",
 "When is the train leaving",
]

for i in range(int(input('Enter num of senteces : '))):
    
    text_=sentences[i]
    trans=Translator()
    result=trans.translate(text_,dest='ar')
    
    sound=gTTS(text=text_,lang='en')
    sound.save(text_+".mp3") 
    

    send()
    ##mail = Mailer(email='gafarasem255@gmail.com',password='gafarasem622')

    print(text_)
	
    # mail.send(receiver='doasem255@gmail.com',  # Email From Any service Provider
    #          subject='LearnEngilsh '+text_,
    #         message=text_+"          "+result.text,
    #         file=path)
   

print("done")
input('   ')