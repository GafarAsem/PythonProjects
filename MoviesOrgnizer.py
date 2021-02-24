from selenium import webdriver
import time
from mailer import Mailer
from googletrans import*
from textblob import TextBlob
import urllib
import requests
import os
path='D:/Movies/'
def getInfoMovie(Movie):
    trans=Translator()
    ##Take the film and open egy best
    inputr=Movie
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


    story1=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[4]/div[2]').text
    story2=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[5]/div[2]').text


    if(len(story1)>5):
        if(str(TextBlob(story1).detect_language())!='ar'):
            story1=trans.translate(story1,dest='ar').text
    if(len(story2)>5):
        if(str(TextBlob(story2).detect_language())!='ar'):
            story2=trans.translate(story2,dest='ar').text
    nameMovie=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[1]/div/h1').text
    rating=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[2]/strong/span').text
    story=story1+" \n "+story2     
    boster=web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[2]/div[1]/div/a/img').get_attribute('src')
    urlmovie=web.current_url
    trailer=web.find_element_by_xpath('//*[@id="yt_trailer"]/div').get_attribute('url')
     
    info={'NameOfMovie':nameMovie,'rating':rating,'story':story,'urlmovie':urlmovie,'trailer':trailer}
    response = requests.get(str(boster))
    os.mkdir(path+nameMovie)
    file = open(path+nameMovie+"/Boster.png", "wb")
    file.write(response.content)
    file.close()
    story=story.split()
    storyon=" \n "
    for i in range(len(story)):
        if(i<=15):
            if(i!=15):
                storyon= storyon+" "+story[i]
            if(i==15):
                storyon= storyon+" "+story[i]+" \n "


        elif (i<=30):
            if(i!=30):
                storyon= storyon+" "+story[i]
            if(i==30):
                storyon= storyon+" "+story[i]+" \n "

        elif (i<=45):
            if(i!=45):
                storyon= storyon+" "+story[i]
            if(i==45):
                storyon= storyon+" "+story[i]+" \n "

        elif (i<=60):
            if(i!=60):
                storyon= storyon+" "+story[i]
            if(i==60):
                storyon= storyon+" "+story[i]+" \n "

        elif (i<=75):
            if(i!=75):
                storyon= storyon+" "+story[i]
            if(i==75):
                storyon= storyon+" "+story[i]+" \n "

        elif (i<=90):
            if(i!=90):
                storyon= storyon+" "+story[i]
            if(i==90):
                storyon= storyon+" "+story[i]+" \n "

        elif (i<=105):
            if(i!=105):
                storyon= storyon+" "+story[i]
            if(i==105):
                storyon= storyon+" "+story[i]+" \n "

        elif (i<=120):
            if(i!=120):
                storyon= storyon+" "+story[i]
            if(i==120):
                storyon= storyon+" "+story[i]+" \n "
            
        
    file = open(path+nameMovie+'/Info Movie.txt',"w+")
    file.write(nameMovie+" \n "+rating+" \n "+storyon+" \n "+urlmovie+" \n "+trailer)
    file.close()
    print(nameMovie+'done')
    
    web.quit()   
    ##exit()       
    ##print(web.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[5]/div[2]').text)
listMovies=[]  
for i in range(len(listMovies)):
    try:
        getInfoMovie(listMovies[i])
    except:
        print(listMovies[i]+"undone")   
print("done all")        