import os
from openai import OpenAI
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    time.sleep(0.1)  # Gives Windows a moment to release the file handle
    os.remove("temp.mp3")

def aiProcess(command):
    # Fixed: Assigned api_key properly and fixed the model name to 'gpt-4o-mini'
    client = OpenAI(api_key="OPENAI_API_KEY")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open wikipedia" in c.lower():
        webbrowser.open("https://wikipedia.org")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play music"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in library.")
    elif c.lower().startswith("search for"):
        query = c.lower().replace("search for", "").strip()
        webbrowser.open(f"https://google.com/search?q={query}")
    elif "news" in c.lower():
        webbrowser.open("https://news.google.com")
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis.....")

    # Keep one global recognizer instead of making a new object every second
    r = sr.Recognizer()

while True:
        try:
            with sr.Microphone() as source:
                print("\nListening for 'Jarvis'...")
                r.adjust_for_ambient_noise(source, duration=1.0)
                audio = r.listen(source, timeout=10, phrase_time_limit=5)

            print("Recognizing...")
            word = r.recognize_google(audio).lower()
            print(f"Heard: '{word}'")

            # Check if the wake word is present anywhere in what you said
            if "jarvis" in word:

                # CASE 1: You said something else along with 'Jarvis' (e.g., "Jarvis open youtube")
                if len(word.strip()) > 6:
                    # Strip out the word 'jarvis' to isolate the command
                    command = word.replace("jarvis", "").strip()
                    print(f"Extracted Command: {command}")
                    processCommand(command)

                # CASE 2: You ONLY said "Jarvis", so it should ask what you want
                else:
                    speak("Yes, how can I help you?")
                    with sr.Microphone() as source:
                        print("Jarvis Active. Listening for your command...")
                        r.adjust_for_ambient_noise(source, duration=0.5)
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)

                        print("Processing command...")
                        command = r.recognize_google(audio).lower()
                        print(f"Command: {command}")

                        processCommand(command)
            else:
                print("Wake word 'Jarvis' not detected. Trying again...")

        except sr.UnknownValueError:
            pass
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print(f"Error: {e}")