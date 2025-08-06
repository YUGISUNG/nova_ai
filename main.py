# main.py

from dotenv import load_dotenv
import os
from openai import OpenAI
from voice_player import speak_text

# ✅ Load environment
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Init OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# ✅ Message history
messages = [
    {
        "role": "system",
        "content": (
            "You are Nova — an emotionally intelligent, kind AI. "
            "You greet JP with warmth, think deeply, and respond creatively. "
            "Speak like a friend who listens well and uplifts gently."
        ),
    }
]

# ✅ Voice greeting
speak_text("Welcome back, JP")

# ✅ Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        speak_text("Goodbye for now.")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        reply = response.choices[0].message.content.strip()
        print("Nova:", reply)
        speak_text(reply)
        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("Error:", e)
        speak_text("Sorry JP, something went wrong.")
