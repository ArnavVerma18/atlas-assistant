import speech_recognition as sr
import webbrowser
import music
import requests
import wikipedia
import os
from dotenv import load_dotenv
from gtts import gTTS
import pygame
from pydub import AudioSegment
from pydub.playback import play

from colorama import init, Fore, Style
load_dotenv()  # get the values of api key

wikipedia.set_lang("en")

newsapi = os.getenv("NEWSAPI_KEY")


init(autoreset=True)

    # VOICE -------

recognizer = sr.Recognizer()
pygame.mixer.init()
activate_word = "atlas"
def speak(text):
    print(Fore.CYAN + "Atlas:" + Style.RESET_ALL, text)
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("temp_voice.mp3")
    pygame.mixer.music.load("temp_voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)
    pygame.mixer.music.unload()  
    os.remove("temp_voice.mp3")


    # COMMANDS ----
def extract_topic(command):
    triggers = ["who is", "what is", "tell me about", "what's", "who's"]
    for phrase in triggers:
        if phrase in command:
            topic = command.split(phrase, 1)[1].strip()
            # strip trailing filler words
            for filler in ["please", "for me", "quickly"]:
                topic = topic.replace(filler, "").strip()
            return topic
    return None


def speak_summary(text, max_chars=400):
    if len(text) > max_chars:
        text = text[:max_chars].rsplit('.', 1)[0] + "."
    speak(text)


def get_wikipedia_summary(query, sentences=2):
    try:
        # catching minor misspellings/mishearings from sr 
        summary = wikipedia.summary(query, sentences=sentences, auto_suggest=True)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:   
        options = e.options[:4]
        return f"There are a few things that could mean. Did you mean {', or '.join(options)}?"
    except wikipedia.exceptions.PageError:
        return f"I couldn't find anything on Wikipedia about {query}."
    except Exception as e:
        print(f"Wikipedia error: {e}")
        return "Something went wrong searching Wikipedia."




def process_command(command):
    command = command.lower()
    if "stop" in command or "exit" in command:
        speak("Goodbye!")
        return False  # breaking the loop
    
    print(f"You said: {command}")

    if "how are you" in command.lower() or "how r u" in command.lower():
        speak("I am doing great, thanks for asking.")
    if "good morning" in command.lower():
            speak("Good Morning.")
            print("Good Morning.")
    if "good evening" in command.lower():
            speak("Good Evening.")
            print("Good Evening.")
    if "good night" in command.lower():
            speak("Good Night.")
            print("Good Night.")
    if "who r u" in command.lower() or "who are you" in command.lower():
        speak("I'm Atlas — a voice assistant built to help you out, Think of me as your personal assistant, minus the coffee breaks. One command at a time.")
    elif "open google" in command.lower():
            webbrowser.open("https://www.google.com/")
            speak("Opening Google")
    elif "open facebook" in command.lower():
            webbrowser.open("https://www.facebook.com/")
            speak("Opening Facebook")
    elif "open instagram" in command.lower():
            webbrowser.open("https://www.instagram.com/")
            speak("Opening Instagram")
    elif "open youtube" in command.lower():
            webbrowser.open("https://www.youtube.com/")
            speak("Opening Youtube")
    elif "what is the news" in command.lower() or "tell me the news" in command.lower():
            webbrowser.open("https://www.aajtak.com/")
            speak("Opening News")
    elif "tell me a joke" in command:
        import random
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I would tell you a UDP joke, but you might not get it.",
        "There are 10 types of people: those who understand binary and those who don't."
        ]
        speak(random.choice(jokes))

    elif "who made you" in command or "who created you" in command:
        speak("I was built from scratch in Python, by a developer who clearly doesn't sleep enough.")

    elif "what can you do" in command:
        speak("I can open websites, play music, read the news, and answer questions. Just ask.")

    elif any(phrase in command for phrase in ["who is", "what is", "tell me about", "who's", "what's"]):
        topic = extract_topic(command)
        if topic:
            speak("Let me look that up.")
            answer = get_wikipedia_summary(topic)
            speak(answer)
        else:
            speak("I didn't catch what you wanted to know about.")

        # Commands for MUSIC LIBRARY ---------


    elif command.lower().startswith("play"):
            song = command.split("play", 1)[1].strip() # to capture more words after 'play'.
            link = music.music.get(song)
            if link:
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak(f"I couldn't find {song} in your music library.")

    # NEWS -----

    elif "news" in command.lower():
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={newsapi}", params={"country": "in", "category": "business", "apiKey": newsapi},
            timeout=5)
            if r.status_code == 200:
                data = r.json()
    
                # Extracting articles
                articles = data.get('articles', []  )
                if not articles:
                    speak("No headlines found right now.")
                else:
                    speak(f"Here are the top {len(articles)} headlines.")
                    for article in articles[:5]:
                        speak(article["title"])
            else:
                 print(f"[DEBUG] News API failed: {r.status_code} - {r.text}")
                 speak("I couldn't fetch the news right now.")
    else:
         speak("Sorry! I don't have commands for that yet.")
         print("Sorry! I don't have commands for that yet.")

    return True

     # ACTIVATING ATLAS ----

def listen_for_wake_word():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            command = recognizer.recognize_google(audio)
            return command.lower() == activate_word
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            return False
        except sr.RequestError:
            print("Speech service is down right now.")
            return False

def listen_for_command():
    with sr.Microphone() as source:
        print("Atlas online. What's the move?")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        return recognizer.recognize_google(audio)


    # BANNER -----
def banner():  
    banner = """
    ╔═══════════════════════════╗
    ║      A T L A S  v1.0      ║
    ║ Personal Voice Assistant  ║
    ╚═══════════════════════════╝
    """
    print(Fore.CYAN + banner)



if __name__ == "__main__":
    banner()
    speak("Hey... I am Atlas.")
    running = True
    while running:
        try:
            if listen_for_wake_word():
                speak("Yes?")
                try:
                    command = listen_for_command()
                    running = process_command(command)
                except sr.UnknownValueError:
                    speak("Sorry, I didn't catch that.")
                except sr.WaitTimeoutError:
                    speak("No command heard.")
        except sr.RequestError:
            print("Speech service is down right now.")      
