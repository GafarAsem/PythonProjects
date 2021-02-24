

import telegram
import json
import requests
from telethon.sync import TelegramClient 
from gtts import gTTS
from googletrans import Translator
import os
import time
from selenium import webdriver
from textblob import TextBlob
  
start =True
Bot='Bot'
my_token='My tocken'
bot='bot'
while start:
    try:
        Bot=telegram.Bot('1389348119:AAFOIMTF-jcXCgjFmAI2aXKeIDqO9wYDFq4')
        my_token = '1389348119:AAFOIMTF-jcXCgjFmAI2aXKeIDqO9wYDFq4'
        bot=requests.get("https://api.telegram.org/bot"+my_token+"/getUpdates")
        x=len(bot.json()['result'])
        start=False
    except:
        j=9
def wrongMessage():
    try:
        Bot.sendMessage(chat_id=idUser,text='للترجمة ارسل كلمة ترجمة وبعدها الجملة بالانجليزية ') 
        Bot.sendMessage(chat_id=idUser,text='للافلام ارسل كلمة فلم  وبعدها اسم الفلم  ')
    except:
        j=0    
def sendMovie(nameOfMovie,iduser):
    web=webdriver.Chrome("D:/Dell/Downloads/Apps/chromedriver.exe")
    try :
        trans=Translator()
        ##Take the film and open egy best
        inputr=nameOfMovie
        
        web.get('https://hola.egybest.co/')

        ##input Name of Movie
        input_=web.find_element_by_xpath('//*[@id="head"]/div/div[2]/form/input[2]')
        input_.send_keys(inputr)
        time.sleep(2)
        ##search

        button1=web.find_element_by_xpath('//*[@id="head"]/div/div[2]/form/i[2]')
        button1.click()
        time.sleep(2)
        ##Open film page
        try:
            button2=web.find_element_by_xpath('//*[@id="movies"]/a/span[2]')
            button2.click()
        except :  
            print()
            

        try:
            button2=web.find_element_by_xpath('//*[@id="movies"]/a/img')
            button2.click()
        except :  
            print()    


        time.sleep(2)    
        time.sleep(10)
        #####################################

        LinkDownload=web.current_url


        story1=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[4]/div[2]').text
        story2=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[5]/div[2]').text


        if(len(story1)>5):
            if(str(TextBlob(story1).detect_language())!='ar'):
                story1=trans.translate(story1,dest='ar').text
        if(len(story2)>5):
            if(str(TextBlob(story2).detect_language())!='ar'):
                story2=trans.translate(story2,dest='ar').text
        
        body=inputr+'''
                                        This is Film '''+LinkDownload+'''
                                        '''+story1+" "+story2+"   "+web.find_element_by_xpath('//*[@id="yt_trailer"]/div').get_attribute('url') 
        url=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[2]/div[1]/div/a/img').get_attribute('src')
        Bot.sendMessage(chat_id=iduser,text=body)  
        Bot.sendPhoto(chat_id=iduser,photo=url)         
        web.quit()                               
    ###########################################################################################
    except:
        wrongMessage()
        web.quit()
def sendtrans(msg,iduser):
    try:
        print('hello')
        texten=msg
        textar=msg
        trans=Translator()
        if(str(TextBlob(msg).detect_language())=='ar'):
            result=trans.translate(msg,dest='en')
            texten=result.text
            textar=msg
        else:
            result=trans.translate(msg,dest='ar')
            textar=result.text
            texten=msg
        print('done')    
        sound=gTTS(text=texten,lang='en')
        sound.save(texten+".mp3") 
        path="D:\\Dell\\Desktop\\Codes\\"+texten+".mp3"
        
        print('done')
        Bot.sendMessage(chat_id=iduser, text=texten+"  \n"+textar)
        Bot.send_audio(chat_id=iduser, audio=open(path, 'rb'))
        os.remove(path)
        print('done')
    except:
        wrongMessage()
def textwhats(phone,iduser):
    try :
        Bot.sendMessage(chat_id=iduser,text="https://api.WhatsApp.com/send?phone="+phone)
    except:
        k=9


while True:
    try:
        bot=requests.get("https://api.telegram.org/bot"+my_token+"/getUpdates")
    except:
        k=9
    if(bot.json()['result']!='[]'):
            
        
        try:    
            msg=bot.json()['result'][x]['message']['text'].split()
            idUser=bot.json()['result'][x]['message']['from']['id']
            msssg=""
            

            
                
            if(str(msg[0])=='movie' or str(msg[0])=='فلم'or str(msg[0])=='فيلم'):
                    
                for i in range(len(msg)):
                    if(i!=0):
                        msssg=msssg+msg[i]+" "
                    
                sendMovie(msssg,idUser)
            elif(str(msg[0])=='trans' or str(msg[0])=='ترجم'or str(msg[0])=='ترجمة'):
                        
                for i in range(len(msg)):
                    if(i!=0):
                        msssg=msssg+msg[i]+" "
                sendtrans(msssg,idUser)  
            elif(str(msg[0])=='whatsapp' or str(msg[0])=='واتس'or str(msg[0])=='واتساب'):
                        
                        
                textwhats(msg[1],idUser)

            elif(str(msg[0])=='off'):
                Bot.sendMessage(chat_id=idUser,text=' سيتم ايقاف تشغيل الكمبوتر بعد مرور دقيقة  ') 
                os.system('shutdown -s')

            elif(str(msg[0])=='restart'):
                Bot.sendMessage(chat_id=idUser,text=' سيتم اعادة تشغيل الكمبوتر بعد مرور دقيقة  ') 
                os.system("shutdown /r /t 1");


            else:
                wrongMessage()
            x=x+1
        except:
            v=8
    ##print(len(bot.json()['result']))


