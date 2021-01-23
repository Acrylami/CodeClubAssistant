
import speech_recognition as sr  # module to mic input
import pyttsx3 as tts  # text-to-speech
import pywhatkit as pwk  # finds songs through YouTube
import datetime  # retrieves dates and times
import wikipedia  # opens Wikipedia pages
import webbrowser as wb
import pyglet  # better audio output

# INITS
listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def play_sound(filePath):
    sound = pyglet.resource.media(filePath)
    sound.play()
    pyglet.app.run()

def getTextFile(file):
    f = open(file, "r")
    return f.read()

def say(string):
    engine.say(string)
    engine.runAndWait()


def take_command():
    try:
        if not sr.Microphone:
            print("Cannot access microphone. See requirements.txt to install PyAudio.")
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if getTextFile("config.txt") in command:
                print("woken...")
                command = command.replace(getTextFile("config.txt"), "")
                return command
    except:
        pass


def run_assistant():
    command = take_command()
    if command is not None:
        print("Debug: " + command)
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
            print(thing)
            try:
                print(wikipedia.summary(thing, 1))
                say(wikipedia.summary(thing, 1))
            except:
                say("sorry, we could not find " + thing + " on Wikipedia. please try again.")


        elif "define" in command:
            thing = command.replace("define", "")
            thing = thing.replace("tofind", "")
            thing = thing.replace(" ", "")
            print(thing)
            try:
                print(wikipedia.summary(thing, 1))
                say(wikipedia.summary(thing, 1))
            except:
                say("sorry, we could not find " + thing + " on Wikipedia. please try again.")


        elif "search wikipedia for" in command:
            thing = command.replace("search wikipedia for", "")
            thing = thing.replace("tofind", "")
            print(thing)
            try:
                print(wikipedia.summary(thing, 1))
                say(wikipedia.summary(thing, 1))
            except:
                say("sorry, we could not find " + thing + " on Wikipedia. please try again.")
        elif "repeat" in command:
            say(command.replace("repeat", ""))

        elif "what does" in command:
            thing = command.replace("what does", "")
            thing = thing.replace("tofind", "")
            thing = thing.replace("mean", "")
            print(thing)
            try:
                print(wikipedia.summary(thing, 1))
                say(wikipedia.summary(thing, 1))
            except:
                say("sorry, we could not find " + thing + " on Wikipedia. please try again.")
                pass
        elif "repeat" in command:
            say(command.replace("repeat", ""))
        elif "bitesize" in command:
            search = command.replace("bitesize", "")
            search = search.replace(" ", "+")
            print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
            say(("searching bbc bite size for %s" % search).replace("+", ""))
            wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)
        elif "research" in command:
            search = command.replace("research", "")
            search = search.replace(" ", "+")
            print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
            say(("searching bbc bite size for %s" % search).replace("+", ""))
            wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)


while True:
    run_assistant()