import speech_recognition as sr     # import the library
 
def getWhatYouSay(duration, offset):                 # initialize recognizer
    with sr.Microphone() as source:  
        r = sr.Recognizer()   # mention source it will be either Microphone or audio files.
        audio = r.record(source, duration=duration, offset=offset)      # listen to the source
        text = r.recognize_google(audio)
        text = text.lower()
        #print(text)    # use recognizer to convert our audio into text part.
        if not text == "":
            return text
        else:
            raise SpeechNotRecognised()