from instabot import Bot 
import time






textmsg1="""قائده في شركه افون العالميه للتجميل 
اقوم بتسجيل الاعضاء وعمل طلبيات لهم من اي منطقه بالسعوديه
 العضويه مجانيه
اكيد سمعتي وجربتي منتجاتها""" 
 
textmsg2="""في  عرووض مرة حلوووووة اذا طلبتي ب 300 حتاخديها ب 225 بس والتوصيل مجاني"""

textmsg3="""وكمان حتكسبي 👇🏻
💛 تكسبي التوصيل مجاني
💚 تكسبي هدية مجانية"""


url= 'هذا الرابط تفرجي وقوليلي \n https://www.avon.com.sa/avon-sa/ebrochure.html'
print('hello')
bot=Bot()
bot.login(username = "umduaaalkethriy55",  
          password = "12345qwert") 
user=bot.get_user_followers('offers_jed3')


for i in range(50):
    bot=Bot()
    bot.login(username = "umduaaalkethriy55",  
          password = "12345qwert") 
    bot.send_message(textmsg1,user[-i])
    

    
    bot=Bot()
    bot.login(username = "umduaaalkethriy55",  
          password = "12345qwert")
    bot.send_message(textmsg2,user[-i])
    


    bot=Bot()
    bot.login(username = "umduaaalkethriy55",  
          password = "12345qwert")
    bot.send_message(textmsg3,user[-i])
    


    bot=Bot()
    bot.login(username = "umduaaalkethriy55",  
          password = "12345qwert")
    bot.send_message(url,user[-i])
    
    print('done',i)

#textg=bot.get_user_following('1j.ft')


