import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1],id)
engine.setProperty('voice',voices[0].id)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Moringing! , Jay")
    elif hour >= 12 and hour < 18:
        speak("Good Aftrnoon! , Jay")
    else:
        speak("Good Evening!, Jay")
    speak("i am jp pc sir, Please tell me how me i help you")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

if __name__=='__main__':
    wishme()
    while True:
        query = take().lower()

        if "wikipedia" in query:
            speak("searching wikipidia....")
            query=query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        elif "open nakri" in query:
            webbrowser.open("https://www.naukri.com/mnjuser/homepage")
        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com/feed/")

        elif "play music" in query:
            music_dir = "E:\\garba\\b_HINDI DJ POP"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The Time Is {strtime}")

        elif 'jay patel' in query:
            str = "Jay patel is a Computer Engineer.he is a jobseeker in this time"
            speak(str)


            