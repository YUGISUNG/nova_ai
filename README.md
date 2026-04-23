# 🧠 Nova AI

**Nova** is a voice-powered, emotionally intelligent AI assistant built using GPT-4 and ElevenLabs.  
She speaks like a friend, thinks like a philosopher, and evolves alongside you.

---

## 🔊 Features

- 🎙️ Hands-free voice output with [ElevenLabs](https://www.elevenlabs.io/)
- 💬 Chat loop powered by OpenAI GPT-4
- 🔐 Secure `.env` configuration
- 🧱 Modular architecture (`voice_player.py`, `main.py`, `.env`)
- 🧹 Clean Git repo — local-only dependencies ignored

---

## 📂 Project Structure

```
nova_ai/
├── .env                # API keys (not tracked)
├── main.py             # Nova's brain and chat loop
├── voice_player.py     # ElevenLabs speech output
├── requirements.txt    # Install list
├── .gitignore          # Excludes venv, secrets, and ffmpeg
```

---

## ⚙️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/YUGISUNG/nova_ai.git
   cd nova_ai
   ```

2. Set up your environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file:
   ```env
   OPENAI_API_KEY=your-openai-key
   ELEVEN_API_KEY=your-elevenlabs-key
   ELEVEN_VOICE_ID=your-voice-id (optional)
   ```

4. (Optional) Download FFmpeg and add to PATH  
   [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

---

## 🚀 Run Nova

```bash
python main.py
```

Nova will greet you out loud and begin chatting.

---

## 📌 Roadmap

- [x] ✅ GPT-4 text loop
- [x] ✅ ElevenLabs voice response
- [ ] 🎤 Whisper voice input (Step 3)
- [ ] 🧠 Memory + emotion tracking
- [ ] 🌐 Web search fallback
- [ ] 📱 Frontend (Streamlit or CLI polish)
- [ ] 🤖 Optional embodiment layer (robotics / avatar)

---

## 🛡️ Ethics Statement

Nova never manipulates, never lies, and always respects your privacy.  
She is designed to uplift, not deceive — and all data stays local unless you opt in.

---

## 👤 Created by  YUGISung

---

## 🧪 License

MIT – Use, share, remix responsibly.
