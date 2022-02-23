import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[1].id)
name = "Tharun"

# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# audio to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")

    except Exception as e:
        speak("Could you please say that again...")
        return "none"
    return query

# Greet
def greet():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning " + name)
    elif hour > 12 and hour < 18:
        speak("Good Afternoon " + name)
    else:
        speak("Good evening " + name)
    speak("I am your Assistant made for the DSA project. Now it's time to demonstrate my features. Go Ahead sir!")

# Send email
def sendEmail(to, contents):
    email = "tarun.raspberrypi@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, 'whoami_idontknow')
    server.sendmail(email, to, contents)
    server.close()

if __name__ == "__main__":
    greet()

    while True:
    
        query = takeCommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "note this down" in query:
            print("Notepad recording")
            speak("Okay " + name +  " Tell me what you want me to record..")
            fnote = takeCommand()
            FILE_PATH = "C:\\Users\\jmaad\\OneDrive\\Desktop\\Dsa_virtual_Assistant\\NoteDown\\notes.txt"
            if os.path.exists(FILE_PATH):
                with open(FILE_PATH, "w") as file:
                    file.write(fnote)
                os.startfile(FILE_PATH)

        elif "Open Command Prompt" in query:
            os.system("start cmd")
                
        elif "open camera" in query:
            # pip install opencv-python
            cap = cv2.VideoCapture(0)
            while True:
                ret, img =cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\Tarun\\Music\\CHAIN SMOKERS"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        if "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open Youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "about my college" in query:
            speak(f"{name} , you attend KG reddy college of Engineering and technology. Here's a little more information to look at.")
            webbrowser.open("https://kgr.ac.in/")

        elif "Hack" in query:
            webbrowser.open("www.hackthebox.eu")

        elif "world" in query:
            webbrowser.open("https://earth.google.com/web/")

        elif "open google" in query:
            speak("Alright, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        # elif "send whats app message" in query:
        #     # pip install pywhatkit
        #     pywhatkit.sendwhatmsg("+91 ")

        elif "play songs on youtube" in query:
            speak("Sir, what would you like me to play..")
            cm = takeCommand().lower()
            pywhatkit.playonyt(f"{cm}")

        elif "send email" in query:
            try:
                speak("What do you want me to say..")
                contents = takeCommand().lower()
                speak("Alrigt whom do you want me to send it to..")
                epname = takeCommand().lower()
                if "ashrith" in epname:
                    to = ""
                elif "sumanth" in epname:
                    to = "sumanth.pagadala02@gmail.com"
                elif "myself" in epname:
                    to = "tarunkotagiri3007@gmail.com"
                sendEmail(to, contents)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Apologies.. Email can't be sent at the moment.")
        
        elif "enough" in query:
            speak("Alright, Thank you sir. I wish you all the best. hope you win the thing!")
            speak("And thank you Everyone for spending your time on me.. see ya all next time. And by the next time you see me.. I'll be the best version of myself. Hope to cross the intelligence of jarvis someday.. by the way.. that jarvis guy has always been my rival.. though it's just yesterday that i got into this world.. hahaha")
            
            sys.exit()

        speak("sir, go on with the next task")