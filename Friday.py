import pyttsx3                      #pip install pyttsx3 --- for text to speech
import datetime                     #inbuilt library
import speech_recognition as sr     #pip install speechRecognition
import wikipedia                    #pip install wikipedia
import smtplib                      #inbuilt library in python.
import webbrowser as wb             #inbuilt library in python.
import os                           #inbuilt library in python.
import pyautogui                    #pip install pyautogui
import psutil                       #pip install psutil
import pyjokes                      #pip install pyjokes
import serial                       #pip install pyserial


#ser = serial.Serial('COM3', 9600)


engine = pyttsx3.init()
#engine.say("Hi this is FRIDAY")    #predefine fuction it convert say function into speech 
#engine.runAndWait()

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()


# speak("Hi this is Friday AI Assistance") #testing...

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
# time()

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
# date()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    print('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)
    print("Battery is at ")
    print(battery.percent)

def jokes():
    speak(pyjokes.get_jokes())

def my_name():
    speak("your name is mayank")

def thank():
    speak( "Your welcome sir! it's my job")

def wishme():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12: 
        speak("Good Morning Sir!")
    elif hour >=12 and hour <18:
        speak("Good afternoon Sir!")
    elif hour >= 18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good night Sir!")
        
    speak("Welcome back")
    time()
    
    date()
    
    speak("Friday at your service. please tell me how can i help you?")
#wishme().


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
        #audio = r.record(source, duration=3)

    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language='en-in')
        #speak(query)    # to speak what we said...
        print(query)    # to print what we said...

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query
#takeCommand()

def sendEmail(to, content ):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rajput7852@mail.com','r@jput7852')
    server.sendmail('rajput7852@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:/All Projects/JARVIS ###########/SS/ss1.jpg")

if __name__ == "__main__":
    wishme()
    while True:
        query  = takeCommand().lower()
        
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'my name' in query:
            my_name()
        
        elif 'thank you' in query:
            thank()

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'search in chrome' in query:
            speak("What should i search ?")
            chromePath = 'C:/Program Files (x86)/Google/Chrome/Application %s'
            search = takeCommand().lower()
            wb.get(chromePath).open_new_tab(search+'.com' )

        elif 'wikipedia' in query:
            speak("Searching...")
            print("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences= 2)
            print(result)
            speak(result)

        elif 'play songs' in query:
            songs_dir = 'D:/Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("what shouldi remember ?")
            data = takeCommand()
            speak("you said me to remember that " +data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Task completed")
        elif 'send email' in query:
            try:
                speak("What shoul I say?")
                content = takeCommand()
                to = 'mayankmrajput01@gmail.com'
                #sendEmail(to, content)
                speak("Email sent succesfully!")
                print("Email sent succesfully!")
                speak(content)
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()
            quit()

        elif 'on' in query:
            speak("Turning on LED")
            ser.write(b'Y')

        elif 'off' in query:
            speak("Turning off LED")
            ser.write(b'N')

        elif 'go Friday' in query:
            speak("bye, call me when you feel lazy.")
            quit()