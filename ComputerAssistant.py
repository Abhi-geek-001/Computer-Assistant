import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
engn = pyttsx3.init()
voices = engn.getProperty('voices')
engn.setProperty('voice', voices[1].id)


def talk(command):
    engn.say(command)
    engn.runAndWait()


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


def run_alexa():
    cmd = take_command()
    if 'date' in cmd:
        dt = datetime.datetime.now().strftime('Today\'s date is %d %B %Y')
        print(dt)
        talk(dt)
    elif 'time' in cmd:
        tm = datetime.datetime.now().strftime('%I %M %p')
        print(tm)
        talk(tm)
    elif 'play' in cmd:
        song = cmd.replace('play', '')
        print("Playing ", song)
        pywhatkit.playonyt(song)
    elif 'joke' in cmd:
        jokes = pyjokes.get_joke()
        talk(jokes)
    elif 'who are you' in cmd:
        engn.say('I am Alexa, your personal assistant.')
        engn.say('What can I do for you?')
        engn.runAndWait()
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
