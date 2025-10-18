def main():
   ...

def open_file(filename):
    with open(f"{filename}.txt","r") as file:
        return(file.read())
    
def count_words(s):
    words = s.split()
    print(len(words))

if __name__ == "__main__":
    main()
    