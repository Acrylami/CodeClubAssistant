import pyglet  # better audio output
import VRFEF
import pyttsx3 as tts
from translate import Translator


engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def say(string):
    engine.say(string)
    engine.runAndWait()

def translateText(input):

    say("What language would you like to translate into?")
    lang = VRFEF.getWhatYouSay(3, 0)
    print(lang)

    say("What would you like to translate?")
    eng = VRFEF.getWhatYouSay(5, 0)
    print(eng)

    say("The translation has been printed")
    print("The translation is: " + Translator.translate(eng, to_lang=lang))
    
    say("Sorry, the language you requested is not recognised.")
    print("Guess what lol")

translateText("cats")