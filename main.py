
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "anjali" in command:
                command = command.replace("anjali", "")
                return command
    except:
        return ""
    return ""

def run_anjali():
    command = take_command()
    if not command:
        return "Sorry, I didn't catch that."

    if "play" in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
        return f"Playing {song}"

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)
        return f"The current time is {time}"

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        talk(info)
        return info

    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)
        return joke

    elif "date" in command:
        talk("Sorry, I have a headache")
        return "Sorry, I have a headache"

    elif "are you single" in command:
        talk("I'm in a relationship with Python")
        return "I'm in a relationship with Python"

    else:
        talk("Please say the command again.")
        return "Please say the command again."
