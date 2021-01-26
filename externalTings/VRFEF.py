import speech_recognition as sr     # import the library
 
def getWhatYouSay():                 # initialize recognizer
    with sr.Microphone() as source:  
        r = sr.Recognizer()   # mention source it will be either Microphone or audio files.
        audio = r.record(source, duration=5, offset=0.5)      # listen to the source
        text = r.recognize_google(audio)
        text = text.lower()
        #print(text)    # use recognizer to convert our audio into text part.
        return text