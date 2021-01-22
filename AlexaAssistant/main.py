import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as pwk
import datetime
import wikipedia

listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def say(string):
    engine.say(string)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                return command
    except:
        pass


def run_alexa():
    command = take_command()
    if command is not None:
        if "play" in command:
            song = command.replace("play", "")
            print("playing" + song)
            say("playing" + song)
            pwk.playonyt(song)

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            say("the time is " + time)

        elif "define" in command:
            thing = command.replace("define", "")
            thing = thing.replace("tofind", "")
            thing = thing.replace(" ", "")
            print(wikipedia.summary(thing, 1))
            say(wikipedia.summary(thing, 1))

        elif "repeat" in command:
            say(command.replace("repeat", ""))


while True:
    run_alexa()
