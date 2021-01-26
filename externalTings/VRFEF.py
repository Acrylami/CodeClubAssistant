import speech_recognition as sr     # import the library
 
def getWhatYouSay():                 # initialize recognizer
    with sr.Microphone() as source:  
        r = sr.Recognizer()   # mention source it will be either Microphone or audio files.
        audio = r.listen(source)        # listen to the source
        text = r.recognize_google(audio)
        text = text.lower()
        #print(text)    # use recognizer to convert our audio into text part.
        return text