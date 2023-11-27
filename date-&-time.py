from datetime import datetime



def time():
    now = datetime.now()
    time_string = now.strftime("so the time is %H:%M:%S right now")
    speak(time_string)

def date():
    now = datetime.now()
    date_string = now.strftime("today's date is %d-%m-%Y")
    speak(date_string)
