from googletrans import Translator
import speech_recognition as sr  # module to mic input
import pyttsx3 as tts  # text-to-speech

translate = Translator()
listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def say(string):
    engine.say(string)
    engine.runAndWait()

def translate(input):
        with sr.Microphone() as source:
            voice = listener.listen(source)
            say("What language would you like to translate into?")
            try:
                lang = listener.recognize_google(voice)
            except:
                lang = ""
            say("What would you like to translate?")
            try:
                eng = listener.recognize_google(voice)
            except:
                eng = ""
            say("The translation has been printed")
            try:
                print("The translation is: " + translate.translate(eng, dest=lang))
            except:
                say("Sorry, the language you requested is not recognised.")