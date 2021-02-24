from twilio.rest import Client 

 
account_sid = 'ACb0cbc83b11af50b92fcf49b1e2f13fdc' 
auth_token = 'ed2848f4703b814c41509d839cd92223'
client = Client(account_sid, auth_token) 
fgo=client.password

url=open('D:/Dell/Desktop/Codes/debug.log')
print(url)
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body="",
                              to='whatsapp:+966552130546' 
                          )

