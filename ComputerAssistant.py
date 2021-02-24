# Importing the modules

import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer() # for listening to audio
engn = pyttsx3.init() # Initilize the audio engine
voices = engn.getProperty('voices') # Uses voices from
engn.setProperty('voice', voices[1].id) # select voice of AI


def talk(command):
    engn.say(command)
    engn.runAndWait()
    
# Command fucntion block

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening ... ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

# function to run bot 
def run_alexa():
    cmd = take_command()
    if 'date' in cmd:
        dt = datetime.datetime.now().strftime('Today\'s date is %d %B %Y') # finds date and time 
        print(dt)
        talk(dt)
    elif 'time' in cmd:
        tm = datetime.datetime.now().strftime('%I %M %p')
        print(tm)
        talk(tm)
        
    #plays music
    elif 'play' in cmd:
        song = cmd.replace('play', '') # 
        print("Playing ", song)
        pywhatkit.playonyt(song)
        
    #random joke
    elif 'joke' in cmd:
        jokes = pyjokes.get_joke()
        talk(jokes)
   
    elif 'who are you' in cmd:
        engn.say('I am Alexa, your personal assistant.')
        engn.say('What can I do for you?')
        engn.runAndWait()
        
    # search wikipedia
    elif 'who is' in cmd:
        prsn = cmd.replace('who is', '')
        info = wikipedia.summary(prsn, 2)
        print(info)
        talk(info)
    else:
        cmd = "Pardon please. I cannot understand your voice."
        talk(cmd)


while True:
    run_alexa()
