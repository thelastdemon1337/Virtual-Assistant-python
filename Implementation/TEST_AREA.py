
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



speak("Alright, Thank you sir. I wish you all the best. hope you win the thing!")
speak("And thank you Everyone for spending your time on me.. see you all next time. And by the next time you see me, I'll be the best version of myself. Hope to cross the intelligence of jarvis someday.. by the way.. that jarvis guy has always been my rival.. though it's just yesterday that i got into this world.. hahaha")