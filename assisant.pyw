# Python program to translate 
# speech to text and text to speech 
  
  
import speech_recognition as sr 
import win32com.client as jl
import webbrowser
import subprocess
import os
import pyttsx3
import datetime


# Initialize the recognizer  
r = sr.Recognizer()  
wsh = jl.Dispatch("WScript.Shell")  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()   

      
      
# Loop infinitely for user to 
# speak 
webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser('C:/Program Files/Google/Chrome/Application/chrome.exe'))
while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
              
            #listens for the user's input  
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
            print("Did you say "+MyText) 

            if(str(MyText)=='keyboard'):
                
                wsh.SendKeys('+%')

            elif str(MyText)=='time english':
                x = datetime.datetime.now()
                SpeakText('month is '+str(x.month))
                SpeakText(' and day is '+str(x.day))
                
                
            elif str(MyText)=='today':
                x = datetime.datetime.now()
                SpeakText(x.strftime("%A"))
                
                

            elif str(MyText)=='open google':
                
                webbrowser.get('chrome').open('google.com')

            elif(str(MyText)=='open microsoft'):
                os.system(r'C:\Users\DELL\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe"')
                
                
            
            
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 

