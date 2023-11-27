
from email.message import EmailMessage
import smtplib
import pyttsx3
import speech_recognition as sr
import pyaudio


r = sr.Recognizer()

tts = pyttsx3.Engine()
def talk(text):
    tts.say(text)
    tts.runAndWait()



def listen():
    with sr.Microphone() as medium:
        print("----JARVIS IS LISTENING ----")
        voice = r.listen(medium, timeout=10)
        data = r.recognize_google(voice)
        print(data)
        return data.lower()





def sendmessage(reciever, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("harsh.hg2005@gmail.com", "udoj zkrm ydxg zsyg")
    em = EmailMessage()
    em['From'] = "harsh.hg2005@gmail.com"
    em['To'] = reciever
    em['subject'] = subject
    em.set_content(body)
    server.send_message(em)

def runsendmessage():
    talk("To whom you want to send your mail ?")
    name = input("ENTER EMAIL ID :")
    reciever = name
    talk("what subject you want to give ?")
#    print("TELL ME YOUR SUBJECT : " , end = " ")
    subject = listen()
    talk("tell me your message you want to send to reciever")
#    print("TELL ME YOUR MESSAGE :" , end = " " )
    body = listen()
    sendmessage(reciever, subject, body)
    print('''\t\t\t\t\t\t\tHURRAY!! 
    \t\t\t\t\tYOUR EMAIL HAS BEEN SENT...''')

def send_bulk_msg(reciever, subject, body):
    for all in reciever:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("harsh.hg2005@gmail.com", "udoj zkrm ydxg zsyg")
        em = EmailMessage()
        em['From'] = "harsh.hg2005@gmail.com"
        em['To'] = all
        em['subject'] = subject
        em.set_content(body)
        server.send_message(em)
def running_bulkmsg():
    talk("To whom you want to send your mail ?")
    name = input("ENTER EMAIL ID :")
    reciever = [name]
    talk("what subject you want to give ?")
#    print("TELL ME YOUR SUBJECT : " , end = " ")
    subject = listen()
    talk("tell me your message you want to send to reciever")
#    print("TELL ME YOUR MESSAGE :" , end = " " )
    body = listen()
    send_bulk_msg(reciever, subject, body)
    talk("Your message has been sent")
    print('''\t\t\t\t\t\t\tHURRAY!! 
    \t\t\t\t\tYOUR EMAIL HAS BEEN SENT...''')
