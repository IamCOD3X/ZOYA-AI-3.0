from tkinter import *
import pyperclip
import webbrowser

#web Browser Settings
chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))


root = Tk()
root.geometry("400x400")
pass_details = StringVar()
myList = []

def devsupport(): 
    b = webbrowser.get('chrome')
    b.open("https://github.com/MIDNIGHT-DEVELOPER/WiFiPasswordViewer")

def see_wifi_pass():
    import subprocess
    global myList
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            myList.append(i)
            myList.append("--")
            myList.append(results[0])
            myList.append("|")
        except IndexError:
            myList.append(i)
            myList.append("--")
            myList.append("")

def show_wifi_pass():
    pass_details.set(myList)


def copytoclipboard():
    password = pass_details.get()
    pyperclip.copy(password)

def on_enter(f):
   SB2.config(background='DarkSlateGray1', foreground= "Black")
def on_leave(f):
   SB2.config(background= 'SystemButtonFace', foreground= 'black')
SB2=Button(root,text="Support",bg="Black" , fg="White" ,font="Arial 8 ",command=devsupport)
SB2.pack(side=BOTTOM)
SB2.bind('<Enter>', on_enter)
SB2.bind('<Leave>', on_leave)



Label(root, text="WIFI Pass Viewer", font="calibri 20 bold").pack()
Button(root, text="Initiate Process Now", command=see_wifi_pass).pack(pady=10)
Button(root, text="Show wifi pass details", command=show_wifi_pass).pack(pady=10)
Entry(root, textvariable=pass_details , width=50).pack(ipady=30)
Button(root, text="Copy to clipbord", command=copytoclipboard).pack(pady=10)

root.mainloop()

