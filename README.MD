Jarvis - Virtual Voice Assistant 🚀
Jarvis is a desktop-based virtual AI assistant built using Python. It uses advanced speech recognition to listen to commands, executes automation tasks like launching websites or searching queries, and leverages OpenAI's GPT-4o-mini API for intelligent conversational responses.

🛠️ Features
Wake Word Activation: Stays idle until it hears the word "Jarvis".

Web Automation: Quick access commands to open popular platforms (Google, YouTube, LinkedIn, GitHub, etc.).

Smart Music Search: Connects with a local custom musicLibrary to play songs.

Web Searching: Supports parsing searches via "search for [your query]".

OpenAI GPT-4o Integration: Answers open-ended questions intelligently with brief, contextual responses.

Optimized Performance: Fully offline Text-to-Speech (TTS) engine for zero-lag communication.

📁 Project Structure
Plaintext
MEGA PROJECT 1- JARVIS/
│
├── main.py          # Main entry point and assistant loop logic
├── musicLibrary.py   # Python dictionary mapping song names to URLs
└── .venv/           # Isolated virtual environment
⚙️ Requirements & Prerequisites
Before running the project, make sure you have Python 3.13+ installed.

1. Install Required System Dependencies
For Windows microphone access, you need PyAudio. If installing it via pip fails, you can install it using:

PowerShell
pip install pyaudio


2. Install Python Packages
Activate your virtual environment and install the required libraries:

PowerShell
# Activate Environment
.venv\Scripts\Activate.ps1

# Install Libraries
pip install pygame numpy speech_recognition openai pyttsx3 requests


## 🚀 Setup & Installation
Clone or copy the project files into a folder named MEGA PROJECT 1- JARVIS.

Open your code terminal inside that directory.

Configure your OpenAI API Key inside main.py under the aiProcess function:

Python
client = OpenAI(api_key="YOUR_SECRET_API_KEY")


## Run the program:

PowerShell
python main.py

## 🗣️ How to Use It
Once initialized, Jarvis will calibrate your microphone acoustics and go into listening mode. You can interact with it in two ways:
  ## Single Breath Command (Fastest):
   "Jarvis open YouTube"
   "Jarvis search for black holes"
  ## Two-Step Interaction:
    Say: "Jarvis"
    Jarvis will reply: "Yes, how can I help you?"
    Say your command: "What is the distance to the moon?"

    