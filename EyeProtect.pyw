from tkinter import *
import time

def close():
    tk.destroy()
while True:
    time.sleep(1200)
    tk=Tk()
    labrl= Label(tk,text="Protect your eye")
    labrl.config(font=("Courier", 44))
    labrl.pack()
    Button(tk,text="Close",command=close,font=("Courier", 44)).pack()
    tk.attributes("-topmost", True)
    tk.mainloop()

