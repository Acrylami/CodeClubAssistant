<<<<<<< Updated upstream
<<<<<<< Updated upstream
import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit as pwk
import datetime
import wikipedia
=======
import speech_recognition as sr # grabs Mic - change to something better
import pyttsx3 as tts # tts
import pywhatkit as pwk # allows you to play songs through
import datetime # gets dates and times
import wikipedia # opens wikipedia links
>>>>>>> Stashed changes

#print("Running") debug because i could not get it to work

#Inits
listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def say(string): # simple say because people lazy to write 2 lines

    engine.say(string)
    engine.runAndWait()
def take_command(): # taking command
    try:
        if not sr.Microphone():
            print("Cannot access microphone. Try installing pyaudio!")
        with sr.Microphone() as source:
            print("I hear you when you're sleeping")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "athena" in command:
                command = command.replace("athena", "")
                return command
    except:
        pass


def run_assistant():
    command = take_command()
    if command is not None:
        print("DEBUG: " + command)
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
    run_assistant()
=======
import installation
try :
    import speech_recognition as sr  # module to mic input
    import pyttsx3 as tts  # text-to-speech
    import pywhatkit as pwk  # finds songs through YouTube
    import datetime  # retrieves dates and times
    import wikipedia  # opens Wikipedia pages
except ImportError:
    installation.installFile("libs.txt")
finally:
    import speech_recognition as sr  # module to mic input
    import pyttsx3 as tts  # text-to-speech
    import pywhatkit as pwk  # finds songs through YouTube
    import datetime  # retrieves dates and times
    import wikipedia  # opens Wikipedia pages

# INITS
listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def say(string):
    engine.say(string)
    engine.runAndWait()
def take_command():
    try:
        if not sr.Microphone:
            print("Cannot access microphone. See requirements.txt to install PyAudio.")
        with sr.Microphone() as source:
            print("I hear you when you're sleeping")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "athena" in command:
                command = command.replace("athena", "")
                return command
    except:
        pass


def run_assistant():
    command = take_command()
    if command is not None:
        print("DEBUG: " + command)
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
    run_assistant()
    print("Running successfully")
>>>>>>> Stashed changes
