import pyfiglet
import shutil
import time
import os

def main():
    ...
   
def greet(s):
    columns = shutil.get_terminal_size().columns
    art = pyfiglet.figlet_format(s, width=columns, justify="center")
    type_effect(art,0.01)

def open_file(filename):
    with open(f"{filename}.txt","r") as file:
        return(file.read())
    
def count_words(s):
    words = s.split()
    print(len(words))

def type_effect(s, delay):
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
    