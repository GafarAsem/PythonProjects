from gtts import gTTS
import os 
import playsound
import speech_recognition as sr
def say(text_) :
    sound=gTTS(text=text_,lang='en')
    sound.save(text_+'.mp3')
    playsound.playsound(text_+'.mp3')
    os.remove(text_+'.mp3')


def WhatIsay():
    
    r=sr.Recognizer()
    source=sr.Microphone()
    audio=r.listen(source)
    said=r.recognize_google()
    print(said)
   


WhatIsay()