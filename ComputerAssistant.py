# Importing modules

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5') #Starting audio
voices = engine.getProperty('voices')
# print(voices[1].id)# to show number of auido and name
engine.setProperty('voice', voices[0].id) # 0 ,1,2,3 are the voices of Bot

# speak function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish me function

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hi, sup man !!")       # Customize it

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# To send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password') # configure email and pass
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # Open YT
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        #Open Google
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # tell the date
        elif "date" in query:
            dt = datetime.datetime.now().strftime('Today\'s date is %d %B %Y')
            print(dt)
            speak(dt)

        # Shares a random programming joke    
        elif 'joke' in query: 
            jokes = pyjokes.get_joke()
            speak(jokes)

        # what can you
        elif 'what can you do' in query:
            speak("For now i can only do the below tasks")
            print("Throw a random joke, Play song , send mail, search wiki , open YT and etc")
            speak ("I will get more functions in future , future is here old man")


        # to play music
                   
        elif 'play music' in query:
            speak("I can't play until i know the path ")
            music_dir = input("Enter your music file path : ")
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        # tell the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # search wikipedia about a person
        elif 'who is' in query:
            prsn = query.replace('who is', '')
            info = wikipedia.summary(prsn, 2)
            print(info)
            speak(info)
            
        # open reddit
        elif 'meme' or 'memes' in query:
            a=1
            while a==1:
                webbrowser.open("https://www.reddit.com/r/memes/")
                a=2

        #sends an email
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To who")
                to = input("Enter email address :")    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Something went upside down")
                print("Things went upside down")

        #Termiates the bot
        elif 'stop listening' in query:
            quit()
        
        # Finished the statement
        else:
            pass
