import os
import speech_recognition as sr
import pyttsx3


#Voice Engine Settings
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening to you...")
        speak("Listening to you...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN' or 'hi-IN')
        print("You said: {}".format(query))
    except:   
        return "none"

while True:

    wake_up = takeCommand()

    if 'wake up' in wake_up:
        speak("STARTING ZOYA")
        os.startfile(r'E:\\Project\\ZOYA GUI\\GUI.py')
    else:
        print("Try Again")
        
    