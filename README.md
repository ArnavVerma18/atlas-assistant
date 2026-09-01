# atlas-assistant
# Atlas — Personal Voice Assistant

<p align="center">
  <img src="demo.gif" width="600" alt="Atlas demo"/>
</p>

Atlas is a wake-word activated voice assistant built entirely in Python. It listens for a spoken activation phrase, interprets voice commands, and responds with natural speech.

## Features

- Wake-word activation — responds only when addressed directly
- Site launcher for common web destinations (Google, YouTube, Instagram, and more)
- Local music playback from a personal song library
- Built-in responses (jokes, status checks, casual conversation)
- Natural voice output via Google Text-to-Speech

## Tech Stack

Python, speech_recognition, gTTS, pygame, requests, python-dotenv

## Setup

\`\`\`bash
git clone https://github.com/yourusername/atlas-voice-assistant.git
cd atlas-voice-assistant
pip install -r requirements.txt
python atlas.py
\`\`\`

## Example Commands

| Command | Action |
|---|---|
| "Atlas" | Activates the assistant |
| "open google" | Opens Google |
| "play [song name]" | Plays from the local music library |
| "tell me a joke" | Tells a joke |
| "stop" | Ends the session |

## Roadmap

- Live news headline integration
- AI-powered responses for open-ended questions
- Multi-turn conversation support

## License

MIT
