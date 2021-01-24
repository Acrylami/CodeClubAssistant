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

list_1 = []
try:
    with open("config.txt") as f:
        for line in f:
            list_1.append(line.strip('\n\r'))
except:
    pass
    print("Failed to initialize\ninsure that 'config.txt' is installed in the same folder as this script")


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
    print("DK why not working. Get main code working first")


def runAthena(self):
    try:
        command = Athena.sampleAudio(self)
        if "play" in command:
            Athena.play(self, command)
        elif "time" in command:
            Athena.time(self, command)
        elif "define" in command:
            Athena.define(self, command)
        elif "search wikipedia for" in command:
            Athena.searchWikipedia(self, command)
        elif "what does" in command:
            Athena.whatdoes(self, command)
        elif "bitesize" in command or "bite size" in command:
            Athena.bitesize(self, command)
        elif "research" in command:
            Athena.reaserch(self, command)
    except:
        print("Error with the play thing\nTypeError: argument of type 'NoneType' is not iterable\nLine 46")


class Athena:
    def sampleAudio(self):
        if not sr.Microphone:
            print("Cannot access microphone. See requirements.txt to install PyAudio.")
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            try:
                command = listener.recognize_google(voice)
            except:
                command = "There was an error with the google recog. Probs one off error just loop and try again"
            finally:
                command = command.lower()

            for x in list_1:
                # Debug line for testing what it hears vs the wake words
                # print(x + " : " + command)
                if x in command or command in x:
                    print("woken...")
                    command = command.replace(x, "")
                    return command

    # FUNCS for what to happen (#DONE was for me, Eoin, to track proggress)
    def play(self, input):  # DONE
        song = input.replace("play", "")
        print("playing" + song)
        say("playing" + song)
        pwk.playonyt(song)

    def time(self, input):  # DONE
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        say("the time is " + time)

    def define(self, input):  # DONE
        thing = input.replace("define", "")
        thing = thing.replace("tofind", "")
        thing = thing.replace(" ", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            say(wikipedia.summary(thing, 1))
        except:
            say("sorry, we could not find " + thing + " on Wikipedia. please try again.")

    def searchWikipedia(self, input):  # DONE
        thing = input.replace("search wikipedia for", "")
        thing = thing.replace("tofind", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            say(wikipedia.summary(thing, 1))
        except:
            say("sorry, we could not find " + thing + " on Wikipedia. please try again.")

    def whatdoes(self, input):  # DONE
        thing = input.replace("what does", "")
        thing = thing.replace("tofind", "")
        thing = thing.replace("mean", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            say(wikipedia.summary(thing, 1))
        except:
            say("sorry, we could not find " + thing + " on Wikipedia. please try again.")
            pass

    # elif "repeat" in command:
    # say(command.replace("repeat", ""))

    def bitesize(self, input):  # DONE

        search = input.replace("bitesize", "")
        search = search.replace(" ", "+")
        search = search.replace("++", "")
        print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
        say(("searching bbc bite size for %s" % search).replace("+", ""))
        wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)

    def reaserch(self, input):
        search = input.replace("research", "")
        search = search.replace(" ", "+")
        print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
        say(("searching bbc bite size for %s" % search).replace("+", ""))
        wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)


while True:
    runAthena(self=Athena())