def displayMenu() -> None:
    print("Options:")
    print("1. Insert word")
    print("2. Show current word")
    print("3. show current word in reverse")
    print("0. Exit")
    return int (input("Your choice: "))


def main() -> None:
    print("Program starting.")
    word = ""
    choice = -1
    while choice != 0:
        choice = displayMenu()
        if choice == 1:
            word = str(input("Insert word: "))
        elif choice == 2:
            print(f"Current word - \"{word}\"")
        elif choice == 3:
            print(f"Word reversed - \"{word[::-1]}\"")
            print("")
        elif choice == 0:
            print("Exiting program.")

        else:
            print("unknown option! Try again.")
            
    print("")
    print("Program ending.")    
    return None


main()
