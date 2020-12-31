import speech_recognition as sr

r = sr.Recognizer()

def take():
    with sr.Microphone() as source:
        print("Listing.....")
        r.pause_threshold = 0.5
        r.energy_threshold = 2000
        audio = r.listen(source)
        print("Recognizing....")
        query = r.recognize_google(audio,language='en')
        print(f"user said {query}")
    return query


while True:
    query = take()

    if "hello how are you" in query:
        print("I am Fine And You")
    else:
        print("Hello , How Are You ?")