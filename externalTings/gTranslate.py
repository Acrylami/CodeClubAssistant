
def gTranslate():
    import pyglet  # better audio outputS
    import pyttsx3 as tts
    from translate import Translator
    import speech_recognition as sr     # import the library
 
    def getWhatYouSay(a, b):                 # initialize recognizer
        with sr.Microphone() as source:  
            r = sr.Recognizer()   # mention source it will be either Microphone or audio files.
            audio = r.record(source, duration=a, offset=b)     # listen to the source
            text = r.recognize_google(audio)
            text = text.lower()
            #print(text)    # use recognizer to convert our audio into text part.
            return text
    engine = tts.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    def say(string):
        engine.say(string)
        engine.runAndWait()

    say("What language would you like to translate into?")
    lang = getWhatYouSay(3, 2)
    lang = lang.split()[0]

    say("What would you like to translate?")
    eng = getWhatYouSay(10, 0)
    print(eng)

    translator = Translator(to_lang =lang, from_lang="English") ##Translator settings
    say("The translation has been printed")
    translated = translator.translate(eng)
    print("The translation is: " + translated)

    
translateText()