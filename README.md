# Timbre 🎵📝

### Video Demo: [https://youtu.be/97bHyNIGS_Y?si=fdjtI00UgyOSM7ow]

Welcome to **Timbre**! This is a Command-Line Audio Toolkit I built for my CS50P Final Project. It's your all-in-one assistant for working with text and speech, powered by some of today's best AI tools.

Ever wanted to turn your notes into a podcast? Or quickly transcribe a voice memo? Timbre makes it easy.

| Feature | Acronym | Powering Tool | Description |
| :--- | :--- | :--- | :--- |
| Text-to-Speech | TTS 🎧 | edge-tts | Bring your text files to life by converting any `.txt` file into natural-sounding speech. |
| Speech-to-Text | STT 🎙️ | openai-whisper | Accurately transcribe audio files into written text. |
| Speech-to-Speech | STS 🔁 | Whisper + edge-tts | Rerecord your audio in a new voice by transcribing and then re-generating the speech. |
| Text Polisher | TP ✨ | Google Gemini API | Supercharge your writing: instantly translate text or polish it for grammar, style, and clarity. |

---

## 🗂️ Folder Structure

```
Timbre/
├── main.py                     # The main CLI script you'll run
├── timbre_module/              # The core Python module with all the logic
│   ├── __init__.py
│   ├── tts.py                  # Handles Text-to-Speech
│   ├── stt.py                  # Handles Speech-to-Text
│   └── polisher.py             # Handles Text Polishing
├── inputs/
│   ├── mp3/                    # Place your input audio files here
│   └── text/                   # Place your input text files here
├── outputs/
│   ├── mp3/                    # All generated audio lands here
│   └── text/                   # All generated text lands here
├── documents/
│   └── voice_list.txt          # A handy list of all supported TTS voices
├── requirements.txt             # All the Python libraries you need
├── LICENSE.txt            
├── .env                        # Where you'll put your secret API key
└── README.md                   # You are here!
```

---

## ⚙️ Installation & Setup

Copy and paste the entire block below to install and set up Timbre:


### 1️⃣ Clone the repository
```bash
git clone https://github.com/thegksingh/Timbre.git
cd Timbre
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment
#### On macOS/Linux:
```bash
source venv/bin/activate
```
#### On Windows:
```bash
.\venv\Scripts\activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Set up your API Key
```bash
echo "GOOGLE_API_KEY=your_actual_key_goes_here" > .env
```

### 6️⃣ System Requirement
- Make sure FFmpeg is installed and added to your system PATH (required for openai-whisper)
- FFmpeg Download & Installation Guide: https://ffmpeg.org/download.html



## 🚀 How to Run Timbre

```bash
# Run the main CLI script
python main.py
```

You’ll see a menu with the following options:

| Option | Acronym | Name | Description |
| ------ | ------- | ---- | ----------- |
| 1      | TTS 🎧  | Text to Speech | Convert written text into spoken audio |
| 2      | STT 🎙️ | Speech to Text | Transcribe spoken audio into text |
| 3      | STS 🔁 | Speech to Speech | Transform audio from one voice into another |
| 4      | TP ✨  | Text Polisher | Translate or polish text for grammar and style |

---

## 💡 Features Explained

### 1️⃣ Text-to-Speech (TTS)
- Converts any `.txt` file from `inputs/text/` into an `.mp3` audio file in `outputs/mp3/`.
- Customize **voice**, **speed (rate)**, and **pitch**.

### 2️⃣ Speech-to-Text (STT)
- Transcribes `.mp3` files from `inputs/mp3/` into `.txt` files in `outputs/text/`.
- Choose the Whisper model (`base`, `small`, `medium`, `large`) for speed vs. accuracy.

### 3️⃣ Speech-to-Speech (STS)
- Two-step process:
  1. Transcribe your audio using STT.
  2. Re-record the text in a new AI voice using TTS.

### 4️⃣ Text Polisher (TP)
- Powered by Gemini API.
- Translate text to another language.
- Polish grammar, fix typos, and rewrite in a specific style (`professional`, `casual`, `academic`).

---

## 📝 Example Usage

### TTS Example
```bash
python main.py
# Then select option 1 (TTS) and follow prompts
# Input file: example.txt
# Output file: example_audio.mp3
# Speaker: en-US-AriaNeural
# Rate: +0%
# Pitch: +0Hz
# Convert text to speech
```

### STT Example
```bash
python main.py
# Then select option 2 (STT) and follow prompts
# Whisper model: base
# Input file: example.mp3
# Output file: example_text.txt
# Transcribe audio to text
```

### STS Example
```bash
python main.py
# Then select option 3 (STS) and follow prompts
# Input file: example.mp3
# Output file: example_audio_new_voice.mp3
# Speaker: en-US-AriaNeural
# Rate: +0%
# Pitch: +0Hz
# Transform audio from one voice to another
```

### Text Polisher Example
```bash
python main.py
# Then select option 4 (TP) and follow prompts
# Enhance or translate text
# Action required: 1 or 2
# Input file: example.txt
# Output file: polished_example.txt
# if chosen 1
# Language to convert:
# if chosen 2 
# Style: professional
```

---

## 📂 Notes
- Python 3.11.9 recommended
- Generated audio files go to `outputs/mp3/` and text files to `outputs/text/`.
- `documents/voice_list.txt` contains all supported TTS voices.
- To run directly, use the provided sample.text and sample.mp3 files in the inputs/text and inputs/mp3 directories.

---

## 🛠️ Future Improvements
- Build a GUI (Tkinter/PyQT) for easier use.
- Add batch processing for multiple files at once.
- Include a "voice preview" feature before generating full audio.

---

## 📜 License
- Built for educational purposes as a CS50P Final Project.  
- Huge thanks to the CS50 team for an amazing course!