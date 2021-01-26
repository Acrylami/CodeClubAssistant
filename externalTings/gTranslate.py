from googletrans import Translator
import pyglet  # better audio output
import VRFEF
import pyttsx3 as tts

engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
translator = Translator()

def say(string):
    engine.say(string)
    engine.runAndWait()

def translateText(input):

    say("What language would you like to translate into?")
    lang = VRFEF.getWhatYouSay()
    print(lang)

    say("What would you like to translate?")
    eng = VRFEF.getWhatYouSay()
    print(eng)

    say("The translation has been printed")
    print("The translation is: " + translator.translate(eng, dest=lang))
    
    say("Sorry, the language you requested is not recognised.")
translateText("cats")