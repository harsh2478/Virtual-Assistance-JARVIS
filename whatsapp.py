import time
import pywhatkit
import speech_recognition as sr
from email_sender import listen
import pyttsx3



def send_whatsapp_sometime():
    print()
    print("##MAKE SURE YOU HAVE LOGIN TO 'web.whatsapp.com' TO AVOID INCONVENIENCE##")
    print()
    pyttsx3.speak("Write the phone number of the receiver. mention country code :")
    number = input("Enter Phone Number of receiver (with country code) :")
    pyttsx3.speak("Now, tell me the message to send to {0}".format(number))
    message = listen()
    pyttsx3.speak("write the time of sending")
    timehrs = input("Hours  :")
    hr = int(timehrs)
    timemin = input("Minutes :")
    min = int(timemin)
    pywhatkit.sendwhatmsg(number, message, hr, min)
    print("done")

def send_whatsapp_instant():
    pyttsx3.speak("Write the phone number of the receiver. mention country code :")
    num = input("Enter Phone Number of receiver (with country code) :")
    pyttsx3.speak("Now, tell me the message to send to {0}".format(num))
    mes = listen()
    pywhatkit.sendwhatmsg_instantly(num, mes)
    print("\t\t\t\t\t \033[1m DONE \033[0m")



