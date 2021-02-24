from pywifi import PyWiFi
from pywifi import Profile, const
import time

def connect():
    profile=Profile()
    profile.ssid='SPEED4G-ECEEF'
    profile.auth = 0
    profile.akm.append(4)
    profile.cipher = 3
    profile.key='B99R80EY41B'

    PyWiFi().interfaces()[0].connect(profile)

while True:
    try:
        time.sleep(3)
        iface = PyWiFi().interfaces()[0].status()
        if(int(iface)==0):
            try:
                connect()
            except:
                print()    
    except :
        print()