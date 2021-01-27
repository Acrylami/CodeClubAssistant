import time
import speech_recognition as sr

def recognizeVoice():
    output = ""
    def callback(recognizer, audio):
        try:
            output = recognizer.recognize_google(audio)
            print(output)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            output = ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            output = ""
        if "athena" in output or "athina" in output:
            output = output.replace("athena", "")
            output = output.replace("athina", "")
    return output

    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source) #calibrates for background audio
    print("Listening...")
    stop_listening = r.listen_in_background(m, callback)
    for i in range(50): 
        time.sleep(0.1)
    stop_listening(wait_for_stop=False)