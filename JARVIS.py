import pyttsx3
import speech_recognition as sr

from email_sender import runsendmessage
from whatsapp import send_whatsapp_instant, send_whatsapp_sometime
from search_webcontent import searchyoutube, googe_search, summary
from search_webcontent import time, date
from weather import weather_api
from email_sender import running_bulkmsg
from chatgpt import chatgpt


jarvis = pyttsx3.init()
voice = jarvis.setProperty('rate', 150)
jarvis.getProperty('voice')
jarvis.say('''Hello Harsh,
    I am Jaarvis, your virtual assistance.
    Tell me, what you want to do? ''')
jarvis.runAndWait()
print("\t\t\t\t \033[4m WELCOME TO YOUR VIRTUAL ASSISTANT MODEL \033[0m")
print("\t\t\t\t\t\t\t \033[4m \033[1m''  JARVIS  ''\033[0m")
print()

while True:
    r = sr.Recognizer()
    input("Press enter for giving a command _")
    with sr.Microphone() as source:
        jarvis.say("Now I am listening sir")
        jarvis.runAndWait()
        print("\033[1m----JARVIS IS LISTENING ----\033[0m")
        r.pause_threshold = 1
        voices = r.listen(source)
        command = r.recognize_google(voices)
        print(command)

        if "whatsapp" and "after" in command:
            send_whatsapp_sometime()

        elif "WhatsApp" in command:
            send_whatsapp_instant()

        elif "tell me" in command:
            command = command.replace("summary", " ")
            f = summary(command)
            print(f)

        elif "hello" in command:
            jarvis.say("Hello Harsh. without wasting time, shall we come to the point?")
            jarvis.runAndWait()

        elif "yes" in command:
            pyttsx3.speak("so please tell me your requirement sir ")

        elif "search" in command:
            googe_search(command)

        elif "play" in command:
            searchyoutube(command)

        elif "send email" in command:
            runsendmessage()

        elif "time" in command:
            time()

        elif "bulk" in command:
            running_bulkmsg()

        elif "date" in command:
            date()
        elif "weather" in command:
            pyttsx3.speak("Here's your area's weather condition")
            weather_api()
            print()

        elif "chat with AI" in command:
            chatgpt()

        elif "you can leave" in command:
            pyttsx3.speak('''okay sir . its great with you. call me whenever you need. Bye-Bye''')
            break

        else:
            pyttsx3.speak('''I am not able to recognise your command sir,
                             tell me something that i am able to search''')
