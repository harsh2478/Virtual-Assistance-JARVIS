import pywhatkit
import pyttsx3
import wikipedia
import wikipedia as googlescrap
from datetime import datetime



def time():
    now = datetime.now()
    time_string = now.strftime("so the time is %H:%M:%S right now")
    speak(time_string)

def date():
    now = datetime.now()
    date_string = now.strftime("today's date is %d-%m-%Y")
    speak(date_string)


jarvis = pyttsx3.init()
def speak(command):
    jarvis.say(command)
    jarvis.runAndWait()

def searchyoutube(command):
    return pywhatkit.playonyt(command)

def summary(command):
    summary = googlescrap.summary(command)
    speak(summary)

def googe_search(command):
    command = command.replace("jarvis", "")
    command = command.replace("google search", "")
    command = command.replace("google", "")
    speak("This is what I found for you")

    try:
        pywhatkit.search(command)
        result = googlescrap.summary(command, 3)
        speak(result)
    except:
        speak("No speakable data available")





