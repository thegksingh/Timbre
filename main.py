import pyfiglet
import shutil
import time

def main():
    ...
   
def greet(s):
    columns = shutil.get_terminal_size().columns
    art = pyfiglet.figlet_format(s, width=columns, justify="center")
    type_effect(art,0.03)

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

if __name__ == "__main__":
    main()
    