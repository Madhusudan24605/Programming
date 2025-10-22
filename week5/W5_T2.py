def frameword(pword):
    print("*" * (len(pword) + 4))
    print(f"* {pword} *")
    print("*" * (len(pword) + 4))
    return None

def main() -> None:
    print("Program starting.")
    word = str(input("Insert word: "))
    print("")
    frameword(word)
    print("")
    print("Program ending.")


main()    
