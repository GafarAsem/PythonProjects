from selenium import webdriver
import time
from mailer import Mailer
from twilio.rest import Client
from googletrans import*
from textblob import TextBlob
trans=Translator()
##Take the film and open egy best
inputr=input("Input your film  : ")
web=webdriver.Chrome("D:/Dell/Downloads/chromedriver.exe")
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


account_sid = 'ACb0cbc83b11af50b92fcf49b1e2f13fdc' 
auth_token = 'ed2848f4703b814c41509d839cd92223' 
client = Client(account_sid, auth_token) 

story1=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[4]/div[2]').text
story2=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[5]/div[2]').text


if(len(story1)>5):
    if(str(TextBlob(story1).detect_language())!='ar'):
        story1=trans.translate(story1,dest='ar').text
if(len(story2)>5):
    if(str(TextBlob(story2).detect_language())!='ar'):
        story2=trans.translate(story2,dest='ar').text
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=inputr+'''
                                       This is Film '''+LinkDownload+'''
                                       '''+story1+" "+story2+"   "+web.find_element_by_xpath('//*[@id="yt_trailer"]/div').get_attribute('url'),
                                          
                              to='whatsapp:+966552130546' ,
                              media_url=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[2]/div[1]/div/a/img').get_attribute('src')
                          )           
web.quit()   
exit()       
##print(web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[5]/div[2]').text)