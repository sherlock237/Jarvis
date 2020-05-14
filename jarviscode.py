import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import ctypes
path = b'C:\\Users\\ACHAL\\Downloads\\jarviss.JPG'
ctypes.windll.user32.SystemParametersInfoA(20, 0, path, 3)
f=open("C:\\Users\\ACHAL\\Desktop\\password.txt","r")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty(voices,voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak('GOOD MORNING')
    elif hour>=12 and hour<18:
        speak('Good AFTERNOON')
    else:
        speak('Good Evening')
    speak('I am Jarvis . please tell me how may I help you') 
def sendEmail(to, content):
    speak('sending')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('achalbhadada55@gmail.com','achal8094551008')
    server.sendmail('achalbhadada55@gmail.com', to, content)
    server.close()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        print("Recognition...")
        query = r.recognize_google(audio,language='en-in')
        print(f'User Said: {query}')
    except:
        print('Say that again Please')
        speak('Say that again Please')
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand()
        query=query.lower()
        print(query)
        if 'Wikipedia' in query:
            speak('searching wikipedia ')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('opening youtube ')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('opening google ')
            webbrowser.open('www.google.com')
        elif 'open stackoverflow' in query:
            speak('opening stackoverflow ')
            webbrowser.open('www.stackoverflow.com')
        elif 'play music' in query:
            speak('sure ')
            webbrowser.open('https://gaana.com/album')
        elif 'open python' in query:
            codePath='C:\\Users\\ACHAL\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw'
            speak('opening python')
            os.startfile(codePath)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I hour %M minutes %S seconds %p") 
            speak(f" the time is {strTime}")
        elif 'send an email' in query:
            try:
                speak("to whom you wanna send sir.")
                to = takecommand()
                speak("what should i say ")   
                content=takecommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry . I am not able to send this email") 
        elif 'by' in query:
            speak("Thanks for using me ")
            exit()
        elif 'shutdown' in query:
            speak("are you sure..")
            shut=takecommand()
            if shut=='yes':
                speak("shutting down .")
                os.system('shutdown /s /t 1')
        elif 'how are you' in query:
            speak('I m good.... what about you ')
        elif 'what can you do' in query:
            speak("i can do lot of things for you.. for example i can send an email i can play music i can open google.. and much more things")
            
               




