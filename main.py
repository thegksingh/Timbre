import pyfiglet
import shutil
import time
import os
from tabulate import tabulate
from timbre_module.tts import tts
import asyncio
from timbre_module.polisher import TextPolisher
import sys

options = [
    ["1.", "TTS", "Text To Speech", "Convert written text into spoken audio."],
    ["2.", "STT", "Speech To Text", "Transcribe spoken aydio into written text"],
    ["3.", "STS", "Speech To Speech", "Transform a user's recorded or TTS voice into different AI-generated voice"],
    ["4.", "TP", "Text Polisher", "Refine and corrects written text from translation,grammer and style"]
]


async def main():
    greet("TIMBER !")
    clear_terminal(2)
    print_option()
    time.sleep(1)
    while True:
        type_effect("How would you like me to proceed? ")
        chosen = input("").strip().lower()
        clear_terminal(0.5)  
        if not chosen:
            type_effect("Please enter your choice (eg., '1' or 'TTS').\n")
        else:
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
                clear_terminal(1)
                type_effect("Processing request...⌛\n")
                try:
                    await speech.generate_audio(text=content, voice=voice, rate=rate, pitch=pitch, output_name=filename)
                    type_effect(f"✅ Processing completed. Find your new audio file at output\mp3\{filename}.mp3\n")
                    sys.exit()
                except Exception as e:
                    type_effect(f"Error: {e}\n")
                    clear_terminal(2)
                    print_option()
                    
                   
            elif chosen== "2" or chosen=="stt":
                type_effect("⚙️Initializing Speech-To-Text...\n")

            elif chosen== "3" or chosen=="sts":
                type_effect("⚙️Initializing Speech-To-Speech...\n")  

            elif chosen== "4" or chosen=="tp":
                polisher = TextPolisher()    
                type_effect("⚙️Initializing Text-Polisher...\n")
                while True:
                    type_effect("Select an action: 1. Translate or 2. Enhance? ")
                    action = input("").strip().lower()
                    clear_terminal(1)
                    if not action:
                        type_effect("Action required\n")
                    else:
                        if action =="1" or action == "translate":
                            content= open_file()
                            type_effect("🌐 Language to convert: ")
                            language = input("")
                            type_effect("📄 output file name: ")
                            filename = input("").strip()
                            clear_terminal(1)
                            type_effect("Processing request...⌛\n")
                            try:
                                result = polisher.translator(text=content, language=language)
                                if result:
                                    type_effect(f"✅ Processing completed. Find your new text file at output\mp3\{filename}.text\n")
                                    sys.exit()                           
                            except Exception as e:
                                type_effect(f"Error: {e}\n")
                                clear_terminal(2)
                        elif action == "2" or action == "enhancer":
                            content= open_file()   
                            type_effect("✨ Enter style: ")
                            style = input("")
                            type_effect("📄 output file name: ")
                            filename = input("").strip()
                            clear_terminal(1)
                            type_effect("Processing request...⌛\n")
                            try:
                                result = polisher.enhancer(text=content, style=style)
                                if result:
                                    type_effect(f"✅ Processing completed. Find your new text file at output\mp3\{filename}.text\n")
                                    break
                            except Exception as e:
                                type_effect(f"Error: {e}\n")
                                clear_terminal(2)
                        else:
                            type_effect("Please enter your action (eg., '1' or 'translate')\n")
                
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

def print_option():
    headers = ["Option", "Acronym", "Name", "Description"]
    table =tabulate(options, headers=headers, tablefmt="fancy_grid")
    columns = shutil.get_terminal_size().columns
    for line in table.splitlines():
        print(line.center(columns))        

if __name__ == "__main__":
    asyncio.run(main())
