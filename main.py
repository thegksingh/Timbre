import pyfiglet
import shutil
import time
import os
from tabulate import tabulate

options = [
    ["1." "TTS", "Text To Speech", "Convert written text into spoken audio."],
    ["2." "STT", "Speech To Text", "Transcribe spoken aydio into written text"],
    ["3." "STS", "Speech To Speech", "Transform a user's recorded or TTS voice into different AI-generated voice"],
    ["4." "TP", "Text Polisher", "Refine and corrects written text from translation,grammer and style"]
]

def main():
    greet("TIMBER !")
    headers = ["Option", "Acronym", "Name", "Description"]
    table =tabulate(options, headers=headers, tablefmt="fancy_grid")
    columns = shutil.get_terminal_size().columns
    for line in table.splitlines():
        print(line.center(columns))

   
def greet(s):
    columns = shutil.get_terminal_size().columns
    art = pyfiglet.figlet_format(s, width=columns, justify="center")
    type_effect(art,0.01)

def open_file():
    while True:
        type_effect("file to open: ")
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
    main()
