# 🤖 Atlas — Personal Voice Assistant

<p align="center">
  <img src="demo.gif" width="600" alt="Atlas demo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" />
  <img src="https://img.shields.io/badge/status-active-brightgreen" />
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" />
</p>

> A wake-word activated voice assistant built in Python — opens websites, plays music, reads live news, and answers open-ended questions using AI.

## ✨ Features

- 🎙️ **Wake-word activation** — responds only when you say "Atlas"
- 🌐 **Site launcher** — Google, YouTube, Instagram, and more
- 🎵 **Music playback** — plays from a local song library
- 📰 **Live news headlines** — pulled from NewsAPI
- 🧠 **AI fallback** — open-ended questions answered via OpenAI
- 🔊 **Natural voice output** — powered by Google Text-to-Speech

## 🛠️ Tech Stack

`Python` · `speech_recognition` · `gTTS` · `pygame` · `OpenAI API` · `NewsAPI`

## 🚀 Setup

\`\`\`bash
git clone https://github.com/yourusername/atlas-voice-assistant.git
cd atlas-voice-assistant
pip install -r requirements.txt
\`\`\`

Create a `.env` file:
\`\`\`
NEWSAPI_KEY=your_key_here
OPENAI_API_KEY=your_key_here
\`\`\`

Run it:
\`\`\`bash
python atlas.py
\`\`\`

## 🗣️ Example Commands

| Say this | Atlas does this |
|---|---|
| "Atlas" | Wakes up |
| "open google" | Opens Google |
| "play [song]" | Plays from your library |
| "news" | Reads today's headlines |
| "tell me a joke" | Cracks a joke |
| "stop" | Ends the session |

## 📄 License
MIT
