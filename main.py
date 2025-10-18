import pyfiglet
import shutil


def main():
    ...
   
def greet(s):
    columns = shutil.get_terminal_size().columns
    art = pyfiglet.figlet_format(s, width=columns, justify="center")
    print(art)

def open_file(filename):
    with open(f"{filename}.txt","r") as file:
        return(file.read())
    
def count_words(s):
    words = s.split()
    print(len(words))

if __name__ == "__main__":
    main()
    