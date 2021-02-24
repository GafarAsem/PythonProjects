import logging
import os
import requests as rqs
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from selenium import webdriver
from textblob.translate import Translator
import time
from textblob import TextBlob
from gtts import gTTS
import telegram
# from numba import njit,prange

bot=telegram.Bot('1389348119:AAFOIMTF-jcXCgjFmAI2aXKeIDqO9wYDFq4')


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

MOVIE, TRANSLATE, VIDEOTUBE, WHATSAAP , PRINT = range(5)



wrongmessage="""/movie - جلب رابط المشاهدة والتحميل و معلومات عن الفيلم
    /translate - لترجمة الجملة والنطق الصحيح لها
    /off - ايقاف تشغيل الكمبيوتر
    /restart - اعادة تشغيل الكمبيوتر
    /weather - حالة الجو في تبوك
    /downtube - لتحميل الفيديوهات من يوتيوب
    """
#################################################################\
# @njit(fastmath=True,cache=True)
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('هلا تقدر تستخدم البوت الحين ')

#shut down pc
# @njit(fastmath=True,cache=True)
def off(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سيتم ايقاف تشغيل الكمبيوتر في غضون دقيقة ")
    os.system('shutdown -s')

#restart pc 
# @njit(fastmath=True,cache=True)
def restart(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text("ستتم اعادة تشغيل الكمبيوتر في غضون دقيقة ")
    os.system('shutdown /r /t 1')
    
    
#get weather in tabuk

def weather(update: Update, context: CallbackContext) -> None:
    # njit(fastmath=True,cache=True)
    update.message.reply_text('سيتم ارسال حالة الطقس في تبوك للان  ')
    ###get weather api
    weather=rqs.get('http://api.openweathermap.org/data/2.5/weather?lat=28.392584&lon=36.584045&appid=4e3d36f8747c07b49c5dfcd4046d8141')
    
    ## Get info from json
    nameCity=str(weather.json()['name'])
    MainWeather =str(weather.json()['weather'][0]['main'])
    
    tempWeather=str(int(weather.json()['main']['temp']-270))
    speedWind=str(weather.json()['wind']['speed'])

    #send info
    update.message.reply_text("المدينة "+nameCity+" \n حالة الطقس"+MainWeather+"\n سرعة الرياح"+speedWind+"\n درجة الحرارة"+tempWeather+"C")

# @njit(fastmath=True,cache=True)
def wrongMessage(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text(wrongmessage)
    return ConversationHandler.END

##################################################################
# @njit(fastmath=True,cache=True)
def GetMovie(update: Update, context: CallbackContext) -> int:

    
    update.message.reply_text("ارسل اسم الفلم ")
    return MOVIE

# @njit(fastmath=True,cache=True)
def SendMovie(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سيتم ارسال معلومات الفلم خلال دقيقة")
    text = update.message.text
    web=webdriver.Chrome("D:/Dell/Downloads/Apps/chromedriver.exe")
    try :
        trans=Translator()
        ##Take the film and open egy best
        inputr=text
        
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
        update.message.reply_text(body)
        update.message.reply_photo(url)         
        web.quit()                               
    ###########################################################################################
    except:
        update.message.reply_text('لم نستطع العثور على هذا الفلم ')
        web.quit()
    return ConversationHandler.END

# @njit(fastmath=True,cache=True)
def GetSentence(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("اكتب الجملة باللغة العربية او الانجليزية")
    return TRANSLATE

# @njit(fastmath=True,cache=True)  
def SendTranslate(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("لحظة ...")
    text = update.message.text
    try:
        
        texten=text
        textar=text
        trans=Translator()
        if(str(TextBlob(text).detect_language())=='ar'):
            result=trans.translate(text,to_lang='en')
            texten=result
            textar=text
        else:
            result=trans.translate(text,to_lang='ar')
            textar=result
            texten=text
            
        sound=gTTS(text=texten,lang='en')
        sound.save(texten+".mp3") 
        path=texten+".mp3"
        
        update.message.reply_text(texten+"  \n"+textar)
        update.message.reply_audio(open(path, 'rb'))
        os.remove(path)
        
    except:
        update.message.reply_text("لم نستطع ايجاد الترجمة حاول مرة اخرى ")
    return ConversationHandler.END

def GetNumper(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("اكتب الرقم مع مفتاح البلد ")
    return WHATSAAP

# @njit(fastmath=True,cache=True)
def SendWhatsapp(update: Update, context: CallbackContext) -> None:
    text="https://api.WhatsApp.com/send?phone="+str(update.message.text)
    update.message.reply_text(text)
    return ConversationHandler.END

# @njit(fastmath=True,cache=True)
def GetFile(update: Update , context: CallbackContext) -> int:
    
    update.message.reply_text(" فضلا ارسل الملف أو الصورة لطباعتها ")
    return PRINT

# @njit(fastmath=True,cache=True)
def PrintDocs(update: Update , context: CallbackContext)-> None:
    file_id=update.message.document.file_id
    file_name=update.message.document.file_name
    newFile = bot.get_file(file_id)

    newFile.download(file_name)
    os.startfile(file_name, "print")
    
    update.message.reply_text("سيتم الان طباعة الملف ")
    return ConversationHandler.END

# @njit(fastmath=True,cache=True)
def PrintPhoto(update: Update , context: CallbackContext)-> None:
    file_id=update.message.photo[0].file_id
    file_name="Photo.jpeg"
    newFile = bot.get_file(file_id)

    newFile.download(file_name)
    os.startfile(file_name, "print")
    
    update.message.reply_text("سيتم الان طباعة الصورة  ")
    return ConversationHandler.END


def main()->None:
    updater = Updater("1389348119:AAFOIMTF-jcXCgjFmAI2aXKeIDqO9wYDFq4", use_context=True)
    dispatcher = updater.dispatcher

    #The commands do not call replay 
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("off", off))
    dispatcher.add_handler(CommandHandler("restart", restart))
    dispatcher.add_handler(CommandHandler("weather", weather))


    #commands with replay

    Movie_handler = ConversationHandler(
        entry_points=[CommandHandler('movie', GetMovie)],
        states={

            MOVIE: [MessageHandler(Filters.text & ~Filters.command, SendMovie)],

        },
        fallbacks=[CommandHandler('cancel', wrongMessage)],
    )

    Trans_handler = ConversationHandler(
        entry_points=[CommandHandler('translate', GetSentence)],
        states={

            TRANSLATE: [MessageHandler(Filters.text & ~Filters.command, SendTranslate)],

        },
        fallbacks=[CommandHandler('cancel', wrongMessage)],
    )

    Whats_handler = ConversationHandler(
        entry_points=[CommandHandler('whatsapp', GetNumper)],
        states={

            WHATSAAP: [MessageHandler(Filters.text & ~Filters.command, SendWhatsapp)],

        },
        fallbacks=[CommandHandler('cancel', wrongMessage)],
    )

    Print_handler= ConversationHandler(
        entry_points=[CommandHandler('print', GetFile)],
        states={

            PRINT: [MessageHandler(Filters.document, PrintDocs)
                    ,MessageHandler(Filters.photo , PrintPhoto)]

        },
        fallbacks=[CommandHandler('cancel', wrongMessage)],
    )

    dispatcher.add_handler(Print_handler)
    dispatcher.add_handler(Whats_handler)
    dispatcher.add_handler(Movie_handler)
    dispatcher.add_handler(Trans_handler)
    bot=telegram.Bot('1389348119:AAFOIMTF-jcXCgjFmAI2aXKeIDqO9wYDFq4')
    # njit(fastmath=True,cache=True)
    updater.start_polling()


if __name__ == '__main__':
    main()
