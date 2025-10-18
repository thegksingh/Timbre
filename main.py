def main():
    ...

def open_file(filename):
    with open(f"{filename}.txt","r") as file:
        return(file.read())
        
if __name__ == "__main__":
    main()
    