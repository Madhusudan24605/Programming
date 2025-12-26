
def readfile(filename) -> str:
    print(f"Reading file '{filename}' content.")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            Content = f.read()
        return Content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""


def writefile(filename, Content) -> None:
    print(f"Writing content into file '{filename}'.")
    with open(filename, "w", encoding="utf-8") as filehandle:
        filehandle.write(Content)
    return None


def main() -> None:
    print("Program starting.")
    print("This program can copy a file.")

    filenamesource = input("Insert source filename: ")
    filenameDestination = input("Insert destination filename: ")

    Content = readfile(filenamesource)

    if Content != "":
        print("File content ready in memory.")
        writefile(filenameDestination, Content)
        print("Copying operation complete.")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()




 

