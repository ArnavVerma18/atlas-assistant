# Atlas 

[Explore Atlas ](https://arnavverma18.github.io/atlas-assistant/)

<i>Personal Voice Assistant • Python Powered • Built From Scratch</i>

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Version-1.0-cyan?style=for-the-badge"> <img src="https://img.shields.io/badge/Voice%20Assistant-ACTIVE-success?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge">

<br><br>
<p align="center">
  <img src="demo.gif" width="600" alt="Atlas demo"/>
</p>
Atlas is a wake-word activated voice assistant built entirely in Python. It listens for a spoken activation phrase, interprets natural voice commands, and responds with synthesized speech — combining web automation, live lookups, and a growing command library into a single conversational interface.

## Features

- **Wake-word activation** — stays idle until addressed directly by name
- **Website launcher** — opens Google, YouTube, Facebook, Instagram, and more on command
- **Wikipedia lookups** — ask "who is..." or "what is..." for concise spoken summaries, with disambiguation handling for ambiguous queries
- **Local music playback** — plays songs from a personal library by voice
- **Built-in personality** — jokes, identity questions, and casual conversation
- **Natural voice output** — powered by Google Text-to-Speech (gTTS)
- **Time-aware greetings** — responds to "good morning," "good evening," and "good night"

## Tech Stack

`Python` · `speech_recognition` · `gTTS` · `pygame` · `wikipedia` · `requests` · `python-dotenv` · `colorama`

## How It Works

Atlas runs a continuous listening loop:

1. Waits silently for the wake word ("Atlas")
2. On activation, listens for a spoken command
3. Routes the command through a matching engine (site launcher, Wikipedia lookup, music library, or built-in responses)
4. Converts the response to speech and plays it back

## Setup

```bash
git clone https://github.com/yourusername/atlas-voice-assistant.git
cd atlas-voice-assistant
pip install -r requirements.txt
```

Create a `.env` file in the project root for any API-dependent features:
