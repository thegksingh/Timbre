import pyfiglet
import shutil
import time
import os
from tabulate import tabulate
from timbre_module.tts import tts
import asyncio

options = [
    ["1.", "TTS", "Text To Speech", "Convert written text into spoken audio."],
    ["2.", "STT", "Speech To Text", "Transcribe spoken aydio into written text"],
    ["3.", "STS", "Speech To Speech", "Transform a user's recorded or TTS voice into different AI-generated voice"],
    ["4.", "TP", "Text Polisher", "Refine and corrects written text from translation,grammer and style"]
]


async def main():
    greet("TIMBER !")
    clear_terminal(2)
    headers = ["Option", "Acronym", "Name", "Description"]
    table =tabulate(options, headers=headers, tablefmt="fancy_grid")
    columns = shutil.get_terminal_size().columns
    for line in table.splitlines():
        print(line.center(columns))
    time.sleep(1)
    while True:
        type_effect("How would you like me to proceed? ")
        chosen = input("").strip().lower()   
        if not chosen:
            type_effect("Please enter your choice (eg., '1' or 'TTS').\n")
        else:
            clear_terminal(0.5)
            if chosen == "1" or chosen == "tts":
                speech = tts()
                type_effect("⚙️ Initializing Text-To-Speech...\n")
                content= open_file()
                type_effect("📄 output file name: ")
                filename = input("").strip()
                type_effect("🔊 Speaker: ")
                voice = input("").strip()
                type_effect("⏱️ Rate: ")
                rate = input("").strip()
                if not rate:
                    rate= "+0%"
                type_effect("🎵 Pitch: ")    
                pitch = input("").strip()
                if not pitch:
                     pitch= "+0Hz"
                type_effect("Processing request...⌛\n")
                try:
                    await speech.generate_audio(text=content, voice=voice, rate=rate, pitch=pitch, output_name=filename)
                    type_effect(f"✅ Processing completed. Find your new audio file at output\mp3\{filename}.mp3\n")
                except Exception as e:
                    type_effect(f"Error: {e}")
                   
            elif chosen== "2" or chosen=="stt":
                type_effect("⚙️Initializing Speech-To-Text...\n")
            elif chosen== "3" or chosen=="sts":
                type_effect("⚙️Initializing Speech-To-Speech...\n")    
            elif chosen== "4" or chosen=="tp":
                type_effect("⚙️Initializing Text-Polisher...\n")
            else:
                type_effect("Please refer to the table above and enter a valid number or acronym.\n")
   
def greet(s):
    columns = shutil.get_terminal_size().columns
    art = pyfiglet.figlet_format(s, width=columns, justify="center")
    type_effect(art,0.01)

def open_file():
    while True:
        type_effect("📄 file to open: ")
        filename = input("")
        try:
            with open(f"inputs\{filename}.txt","r") as file:
                file_content = file.read()
                if len(file_content) != 0:
                    return(file_content)
                else:
                    type_effect(f"{filename} is empty!\n")
                    clear_terminal()
        except FileNotFoundError:
            type_effect(f"{filename} does not exits!\n")
            clear_terminal()

def count_words(s):
    words = s.split()
    print(len(words))

def type_effect(s, delay=0.1):
    for character in s:
        print(character, end="", flush=True)
        time.sleep(delay)

def clear_terminal(delay=1):
    time.sleep(delay)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    asyncio.run(main())
