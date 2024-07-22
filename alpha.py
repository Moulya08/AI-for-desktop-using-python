import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit
import requests

engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alpha mam, Please tell me how can i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query    


def get_news():
    news_headlines = []
    results = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey=c105f268b0fe4889965ee11c0c8c0387").json()
    articles = results["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:6]



if __name__ == "__main__":
    wishMe() 
    #while True:
    if 1:    
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:    
            webbrowser.open("youtube.com")

        elif 'open google' in query:    
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\admin\\Music"
            Songs = os.listdir(music_dir)
            print(Songs)
            os.startfile(os.path.join(music_dir, Songs[0]))

        elif 'tell joke' in query:
            speak(pyjokes.get_joke())

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'give news' in query:
            speak(f"I am reading the latest headline of today,mam")
            speak(get_news())
            print(*get_news(),sep='\n')
            
    

