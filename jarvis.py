# ================= IMPORTS =================
import datetime
import wikipedia
import webbrowser
import sys
import random

# ================= SPEAK =================
def speak(text):
    print("Jarvis:", text)

# ================= LISTEN =================
def listen():
    try:
        return input("You: ").lower()
    except:
        return ""

# ================= GREETING =================
def greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning")
    elif hour < 17:
        speak("Good afternoon")
    else:
        speak("Good evening")

# ================= JOKE =================
def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the computer go to the doctor? Because it caught a virus.",
        "Why was the math book sad? Because it had too many problems."
    ]
    speak(random.choice(jokes))

# ================= MOTIVATION =================
def motivation():
    quotes = [
        "Believe in yourself and keep going.",
        "Small steps every day lead to big success.",
        "Hard work always pays off."
    ]
    speak(random.choice(quotes))

# ================= CALCULATOR =================
def calculator(task):
    try:
        nums = [int(s) for s in task.split() if s.isdigit()]
        if len(nums) < 2:
            speak("Please provide two numbers")
            return

        if "add" in task:
            speak(f"Result is {nums[0] + nums[1]}")
        elif "subtract" in task:
            speak(f"Result is {nums[0] - nums[1]}")
        elif "multiply" in task:
            speak(f"Result is {nums[0] * nums[1]}")
        elif "divide" in task:
            speak(f"Result is {nums[0] / nums[1]}")
        else:
            speak("Please say a valid calculation")
    except:
        speak("Calculation error")

# ================= WAKE WORD =================
def wait_for_wake():
    while True:
        command = listen()
        if "hey jarvis" in command:
            speak("Yes, I am ready")
            break

# ================= MAIN =================
speak("Jarvis system online. Say hey jarvis to activate")

while True:
    wait_for_wake()
    task = listen()

    if not task:
        speak("Please repeat")
        continue

    # EXIT
    if "exit" in task or "bye" in task:
        speak("Goodbye")
        sys.exit()

    # GREETING
    elif "how are you" in task or "good morning" in task:
        greeting()

    # TIME
    elif "time" in task:
        speak(datetime.datetime.now().strftime("The time is %I:%M %p"))

    # DATE
    elif "date" in task:
        speak(datetime.datetime.now().strftime("Today is %d %B %Y"))

    # DAY
    elif "day" in task:
        speak(datetime.datetime.now().strftime("Today is %A"))

    # MONTH
    elif "month" in task:
        speak(datetime.datetime.now().strftime("Current month is %B"))

    # OPEN WEBSITES
    elif "open google" in task:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in task:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in task:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "open linkedin" in task:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    # WEATHER
    elif "weather" in task:
        speak("Opening weather report")
        webbrowser.open("https://www.google.com/search?q=weather")

    # PLAY SONG
    elif task.startswith("play"):
        song = task.replace("play", "").strip()
        if song:
            speak(f"Playing {song} on YouTube")
            url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
            webbrowser.open(url)
        else:
            speak("Please tell the song name")

    # JOKE
    elif "joke" in task:
        tell_joke()

    # MOTIVATION
    elif "motivate" in task or "motivation" in task:
        motivation()

    # CALCULATOR
    elif any(word in task for word in ["add", "subtract", "multiply", "divide"]):
        calculator(task)

    # WIKIPEDIA
    else:
        try:
            speak(wikipedia.summary(task, sentences=2))
        except:
            speak("Sorry, I could not find information on that")
