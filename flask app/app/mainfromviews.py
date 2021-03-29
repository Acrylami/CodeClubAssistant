import pyttsx3
import speech_recognition as sr  # module to mic input
import pyttsx3 as tts  # text-to-speech
import pywhatkit as pwk  # finds songs through YouTube
import datetime  # retrieves dates and times
import wikipedia  # opens Wikipedia pages
import webbrowser as wb
import pyglet  # better audio output
from translate import Translator
import importlib
import time

listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Calculator FUNCS:

# All in radius
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

# Basic
add = lambda a, b: a + b
minus = lambda a, b: a - b
times = lambda a, b: a * b
divide = lambda a, b: a / b

# More less Basic
power = lambda a, b: a ** b
root = lambda a, b: a ** (b ** -1)

# BrainBogglers
cArea = lambda a: pi * (a ** 2)  # circle Area
cCum = lambda a: (a * 2) * pi  # circle circumference
ciArea = lambda a, b: ((pi * (a ** 2)) * 2) + ((a * 2) * pi)  # cylinder area
ciVol = lambda a, b: (pi * (a ** 2)) * b  # cylinder volume

# GigaBogglers
sArea = lambda a: 4 * pi * (a ** 2)
sVol = lambda a: (4 / 3) * pi * (a ** 3)

skipTranslation = False


def play_sound(filePath):
    sound = pyglet.resource.media(filePath)
    sound.play()
    pyglet.app.run()


def speakPhrase(string):
    importlib.reload(tts)
    engine = tts.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    tts.speak(string)


class Athena:
    def runAthena(self):
        try:

            if not sr.Microphone:
                print("Cannot access microphone. See requirements.txt to install PyAudio.")
            with sr.Microphone() as source:
                print("listening...")
                voice = listener.listen(source)
                text = listener.recognize_google(voice, language='en-UK')
                Athena.processText(self, text)
        except:
            pass

    def processText(self, text):
        print(text)
        text = text.lower()
        text = "athena" + text
        print("woken...")
        if "athena" in text or "athina" in text:
            text = text.replace("athena", "")
            text = text.replace("athina", "")

            print(text)

            if "play" in text:
                Athena.play(self, text)
            elif "time" in text:
                Athena.time(self, text)
            elif "define" in text:
                Athena.define(self, text)
            elif "search wikipedia for" in text:
                Athena.searchWikipedia(self, text)
            elif "what does" in text:
                Athena.whatdoes(self, text)
            elif "bitesize" in text or "bite size" in text:
                Athena.bitesize(self, text)
            elif "research" in text:
                Athena.research(self, text)
            elif "translate" in text:
                Athena.translationModule(self, text)
            elif "calculate" in text or "what's" in text:
                Athena.run_calculator(self, text)
            else:
                pass


    def play(self, input):
        song = input.replace("play", "")
        print("playing" + song)
        speakPhrase("playing" + song)
        pwk.playonyt(song)

    def time(self, input):
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        speakPhrase("the time is " + time)

    def define(self, input):
        thing = input.replace("define", "")
        thing = thing.replace("tofind", "")
        thing = thing.replace(" ", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            speakPhrase(wikipedia.summary(thing, 1))
        except:
            speakPhrase("sorry, we could not find " + thing + " on Wikipedia. please try again.")

    def searchWikipedia(self, input):
        thing = input.replace("search wikipedia for", "")
        thing = thing.replace("tofind", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            speakPhrase(wikipedia.summary(thing, 1))
        except:
            speakPhrase("sorry, we could not find " + thing + " on Wikipedia. please try again.")

    def whatdoes(self, input):
        thing = input.replace("what does", "")
        thing = thing.replace("tofind", "")
        thing = thing.replace("mean", "")
        print(thing)
        try:
            print(wikipedia.summary(thing, 1))
            speakPhrase(wikipedia.summary(thing, 1))
        except:
            speakPhrase("sorry, we could not find " + thing + " on Wikipedia. please try again.")
            pass

    def bitesize(self, input):
        search = input.replace("bitesize", "")
        search = search.replace(" ", "+")
        search = search.replace("++", "")
        print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
        speakPhrase(("searching bbc bite size for %s" % search).replace("+", ""))
        wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)

    def research(self, input):
        search = input.replace("research", "")
        search = search.replace(" ", "+")
        print(("Searching BBC Bitesize for '%s'" % search).replace("+", ""))
        speakPhrase(("searching bbc bite size for %s" % search).replace("+", ""))
        wb.open("https://www.bbc.co.uk/bitesize/search?q=%s" % search)

    def translationModule(self, input):
        string = input
        string = string.replace("translate", "")
        string = string.replace("  ", "")
        string = string.replace(" into ", "|")
        stringSplit = string.split("|", 1)
        eng = stringSplit[0]
        lang = stringSplit[1]

        translator = Translator(to_lang=lang, from_lang="English")  ##Translator settings
        translated = translator.translate(eng)
        print("The translation is: " + translated)
        try:
            speakPhrase(translated)
        except:
            print("The output language is not supported in speech")
            speakPhrase("The output language is not supported in speech")

    def run_calculator(self, text):
        text = text.replace("calculate", "")
        text = text.replace("what's", "")
        text = text.replace("add", "+")
        text = text.replace("minus", "-")
        text = text.replace("divided by", "/")
        text = text.replace("times", "x")
        text = text.replace("to the power of", "^")
        if "+" in text:
            text = text.replace("+", " ")
            text = text.split()
            a = int(text[0])
            b = int(text[1])
            answer = add(a, b)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "-" in text:
            text = text.replace("-", "")
            text = text.split()
            a = int(text[0])
            b = int(text[1])
            answer = minus(a, b)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "x" in text:
            text = text.replace("x", "")
            text = text.split()
            a = int(text[0])
            b = int(text[1])
            answer = times(a, b)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "/" in text:
            text = text.replace("/", "")
            text = text.split()
            a = int(text[0])
            b = int(text[1])
            answer = divide(a, b)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "^" in text:
            text = text.replace("^", "")
            text = text.split()
            a = int(text[0])
            b = int(text[1])
            answer = power(a, b)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "squared" in text:
            text = text.replace("squared", "")
            text = text.split()
            a = int(text[0])
            answer = power(a, 2)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "cubed" in text:
            text = text.replace("cubed", "")
            text = text.split()
            a = int(text[0])
            answer = power(a, 3)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "root" in text:
            text = text.replace("to the", "")
            text = text.replace("th", "")
            text = text.replace("st", "")
            text = text.replace("nd", "")
            text = text.replace("second", "2")
            text = text.replace("rd", "")
            text = text.replace("root", "")
            text = text.replace("route", "")
            text = text.split()
            a = int(text[0])
            b = int(text[1])
            answer = root(a, b)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "square" in text:
            text = text.replace("square root of", "")
            text = text.split()
            a = int(text[0])
            answer = root(a, 2)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)

        elif "cube" in text:
            text = text.replace("cube root of", "")
            text = text.split()
            a = int(text[0])
            answer = root(a, 3)
            try:
                speakPhrase("The answer is " + str(answer))
            except:
                print("The answer is", answer)


Athena.runAthena(self=Athena)
