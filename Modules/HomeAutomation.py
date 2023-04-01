from tkinter import *
from time import sleep
import serial
import webbrowser
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#setting up bluetooth connection
ser = serial.Serial('COM6', 9600 ,bytesize=8 , timeout=1) #change COM Port , baudrate , timeout acc. to your need

#setting up chrome [path]
chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))


####FUNCTIONS

def devsupport(): 
   print("Opening Support Website")
   speak("Opening Support Website")
   b = webbrowser.get('chrome')
   b.open("www.github.com/IamCOD3X/HomeAutomation")

def all_on():
   print("Turning All Switchs ON")
   
   sleep(0.1) 
   ser.write(b'Z')
   speak("Turning All Switchs ON")

def all_off():
   print("Turning All Switchs OFF")
   
   sleep(0.1) 
   ser.write(b'z')
   speak("Turning All Switchs OFF")

def S1_on():
   print("Turning ON Switch 4")
   sleep(0.1) 
   ser.write(b'A')
   speak("Turning ON Switch 4")

def S1_off():
   print("Turning OFF Switch 4")
   sleep(0.1) 
   ser.write(b'a')
   speak("Turning OFF Switch 4")

def S2_on():
   print("Turning ON Switch 3")
   sleep(0.1) 
   ser.write(b'B')
   speak("Turning ON Switch 3")

def S2_off():
   print("Turning OFF Switch 3")
   sleep(0.1) 
   ser.write(b'b')
   speak("Turning OFF Switch 3")

def S3_on():
   print("Turning ON Switch 2")
   sleep(0.1) 
   ser.write(b'C')
   speak("Turning ON Switch 2")

def S3_off():
   print("Turning OFF Switch 2")
   sleep(0.1) 
   ser.write(b'c')
   speak("Turning OFF Switch 2")

def S4_on():
   print("Turning ON Switch 1")
   sleep(0.1) 
   ser.write(b'D')
   speak("Turning ON Switch 1")

def S4_off():
   print("Turning OFF Switch 1")
   sleep(0.1) 
   ser.write(b'd')
   speak("Turning OFF Switch 1")



root=Tk()
root.title=("Home Automation Utility")
root.geometry("600x300")
root.minsize(600,300)
root.maxsize(600,300)

L1= Label(text="Home Automation Utility" , fg="Black", font="Aquarilla 20 ", relief=SUNKEN)
L1.pack()
L1.place(x=155,y=0)
L= Label(text="By CODEX" , fg="Black", font="Aquarilla 5 ", relief=SUNKEN)
L.pack()
L.place(x=450,y=40)


'''//////////////////////////////////////////////////////////////////////'''



F0= Frame(root, borderwidth=3 , bg="Black", relief=SUNKEN )
F0.pack(side=BOTTOM , anchor=CENTER)
F0.place(x=293 ,y=80)

def on_enter(f):
   S1.config(background='Green')
def on_leave(f):
   S1.config(background= 'SystemButtonFace', foreground= 'black')
S1=Button(F0,text="ON",bg="Black", fg="White" , width=10 ,command=S1_on)
S1.pack(side=BOTTOM)
S1.bind('<Enter>', on_enter)
S1.bind('<Leave>', on_leave)



def on_enter(f):
   S2.config(background='Green')
def on_leave(f):
   S2.config(background= 'SystemButtonFace', foreground= 'black')
S2=Button(F0,text="ON",bg="Black", fg="White" , width=10 ,command=S2_on)
S2.pack(side=BOTTOM)
S2.bind('<Enter>', on_enter)
S2.bind('<Leave>', on_leave)



def on_enter(f):
   S3.config(background='Green')
def on_leave(f):
   S3.config(background= 'SystemButtonFace', foreground= 'black')
S3=Button(F0,text="ON",bg="Black", fg="White" , width=10 ,command=S3_on)
S3.pack(side=BOTTOM)
S3.bind('<Enter>', on_enter)
S3.bind('<Leave>', on_leave)



def on_enter(f):
   S4.config(background='Green')
def on_leave(f):
   S4.config(background= 'SystemButtonFace', foreground= 'black')
S4=Button(F0,text="ON",bg="Black", fg="White" , width=10 ,command=S4_on)
S4.pack(side=BOTTOM)
S4.bind('<Enter>', on_enter)
S4.bind('<Leave>', on_leave)



def on_enter(f):
   S5.config(background='Green')
def on_leave(f):
   S5.config(background= 'SystemButtonFace', foreground= 'black')
S5=Button(F0,text="ALL ON",bg="Black", fg="White" , width=10 ,command=all_on)
S5.pack(side=BOTTOM)
S5.bind('<Enter>', on_enter)
S5.bind('<Leave>', on_leave)

'''/////////////////////////////////////////////////////////////////////'''

F1= Frame(root, borderwidth=3 , bg="Black", relief=SUNKEN )
F1.pack(side=BOTTOM , anchor=CENTER)
F1.place(x=378 ,y=80)

def on_enter(f):
   S11.config(background='RED')
def on_leave(f):
   S11.config(background= 'SystemButtonFace', foreground= 'black')
S11=Button(F1,text="OFF",bg="Black", fg="White" , width=10 ,command=S1_off)
S11.pack(side=BOTTOM)
S11.bind('<Enter>', on_enter)
S11.bind('<Leave>', on_leave)


def on_enter(f):
   S22.config(background='RED')
def on_leave(f):
   S22.config(background= 'SystemButtonFace', foreground= 'black')
S22=Button(F1,text="OFF",bg="Black", fg="White" , width=10 ,command=S2_off)
S22.pack(side=BOTTOM)
S22.bind('<Enter>', on_enter)
S22.bind('<Leave>', on_leave)



def on_enter(f):
   S33.config(background='RED')
def on_leave(f):
   S33.config(background= 'SystemButtonFace', foreground= 'black')
S33=Button(F1,text="OFF",bg="Black", fg="White" , width=10 ,command=S3_off)
S33.pack(side=BOTTOM)
S33.bind('<Enter>', on_enter)
S33.bind('<Leave>', on_leave)



def on_enter(f):
   S44.config(background='RED')
def on_leave(f):
   S44.config(background= 'SystemButtonFace', foreground= 'black')
S44=Button(F1,text="OFF",bg="Black", fg="White" , width=10 ,command=S4_off)
S44.pack(side=BOTTOM)
S44.bind('<Enter>', on_enter)
S44.bind('<Leave>', on_leave)



def on_enter(f):
   S55.config(background='RED')
def on_leave(f):
   S55.config(background= 'SystemButtonFace', foreground= 'black')
S55=Button(F1,text="ALL OFF",bg="Black", fg="White" , width=10 ,command=all_off)
S55.pack(side=BOTTOM)
S55.bind('<Enter>', on_enter)
S55.bind('<Leave>', on_leave)

##############################

def on_enter(f):
   exitb.config(background='RED')
def on_leave(f):
   exitb.config(background= 'SystemButtonFace', foreground= 'black')
exitb=Button(root,text="EXIT",bg="Black", fg="White" , width=10 ,command=exit)
exitb.pack(side=BOTTOM)
exitb.bind('<Enter>', on_enter)
exitb.bind('<Leave>', on_leave)



'''////////////////////////////////////////////////////////////////////////'''

F2= Frame(root, borderwidth=3 , bg="Black", relief=SUNKEN )
F2.pack(side=BOTTOM , anchor=CENTER)
F2.place(x=138 ,y=80)

L0= Label(F2, text="All ON/OFF", bg="white",width=16, fg="black", font="Voltec 11")
#L0.pack()
#L0.place(x=220,y=60)
L0.grid(pady=2)

L1= Label(F2, text="Switch 1", bg="white", width=16 , fg="black", font="Voltec 11 ")
#L1.pack()
L1.grid(pady=1)

L2= Label(F2, text="Switch 2", bg="white" ,width=16, fg="black", font="Voltec 11 ")
L2.grid(pady=1)

L3= Label(F2, text="Switch 3", bg="white" ,width=16, fg="black", font="Voltec 11 ")
#L3.pack()
L3.grid(pady=1)

L4= Label(F2, text="Switch 4", bg="white" ,width=16, fg="black", font="Voltec 11 ")
#L4.pack()
L4.grid(pady=2)

Fx= Frame(root, borderwidth=3 , bg="Black")
Fx.pack(side=BOTTOM , anchor=CENTER)
Fx.place(x=550 ,y=270)

def on_enter(f):
   SB2.config(background='DarkSlateGray1', foreground= "Black")
def on_leave(f):
   SB2.config(background= 'SystemButtonFace', foreground= 'black')
SB2=Button(Fx,text="Support",bg="Black" , fg="White" ,font="Arial 8 ",command=devsupport)
SB2.pack(side=LEFT)
SB2.bind('<Enter>', on_enter)
SB2.bind('<Leave>', on_leave)

root.mainloop()