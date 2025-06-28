from flask import Flask, render_template, request, jsonify
import datetime
import pywhatkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '').lower()

    if "hi" in question or "hello" in question:
        return jsonify({'answer': "Hello! How can I assist you today?"})
    
    elif "good morning" in question or "good afternoon" in question or "good evening" in question:
        return jsonify({'answer': "Wishing you a pleasant day!"})
    
    elif "how are you" in question:
        return jsonify({'answer': "I'm just code, but I'm feeling great! How about you?"})
    
    elif "time" in question:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return jsonify({'answer': f"The current time is {current_time}."})
    
    elif "date" in question:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        return jsonify({'answer': f"Today is {today}."})
    
    elif "greeting" in question or "greet me" in question:
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            greet = "Good Morning!"
        elif 12 <= hour < 17:
            greet = "Good Afternoon!"
        elif 17 <= hour < 21:
            greet = "Good Evening!"
        else:
            greet = "Good Night!"
        return jsonify({'answer': greet})
    
    elif "weather" in question:
        return jsonify({'answer': "Please use a weather app for accurate updates. I’ll include this soon!"})
    
    elif "play" in question:
        song = question.replace("play", "").strip()
        pywhatkit.playonyt(song)
        return jsonify({'answer': f"Playing {song} on YouTube."})
    
    elif "reminder" in question:
        return jsonify({'answer': "I can't store reminders yet, but I'm learning quickly!"})
    
    elif "your name" in question:
        return jsonify({'answer': "I am Anjali, your personal voice assistant."})
    
    elif "thank you" in question:
        return jsonify({'answer': "You're welcome!"})
    
    elif "open google" in question:
        pywhatkit.search("Google")
        return jsonify({'answer': "Opening Google."})
    
    elif "open youtube" in question:
        pywhatkit.playonyt("YouTube")
        return jsonify({'answer': "Opening YouTube."})
    
    elif "open linkedin" in question:
        pywhatkit.search("Linkedin")
        return jsonify({'answer': "Opening LinkedIn."})
    
    else:
        return jsonify({'answer': "Sorry, I didn't understand that. Try asking something like 'what's the time' or 'play a song'."})

if __name__ == '__main__':
    app.run(debug=True)
