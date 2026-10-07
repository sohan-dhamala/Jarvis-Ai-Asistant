import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
def say(text):
    print(f"AI :  {text}")
    if "[system]" in text : return
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def query():
    # user_input = input("You: ")
    # return user_input if user_input else ""
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic,duration=1)
        print("Listening...")
        
        
        while True:
               try:
                   audio = r.listen(mic)
                   text = r.recognize_google(audio)
                   print(text.lower())
                   if text:
                    return text
               except sr.UnknownValueError:
                   pass