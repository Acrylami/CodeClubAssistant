# Fixed bugs
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


def say(string):
    engine.say(string)
    engine.runAndWait()


def take_command():
    list_1 = []
    try:
        with open("config.txt") as f:
            for line in f:
                list_1.append(line.strip('\n\r'))
        if not sr.Microphone:
            print("Cannot access microphone. See requirements.txt to install PyAudio.")
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            for x in list_1:
                #Debug line for testing what it hears vs the wake words
                #print(x + " : " + command)
                if command in x or x in command:
                    print("woken...")
                    command = command.replace(x, "")
                    return command
    except:
        pass


def run_assistant():
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

        elif "bitesize" in command or "bite size" in command:
            search = command.replace("bitesize", "")
            search = search.replace(" ", "+")
            search = search.replace("++", "")
            print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
            say(("searching bbc bite size for %s" % search).replace("+", ""))
            wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)


while True:
    run_assistant()
