def askName() -> str:
    name = str(input("Insert name: "))
    return name

def greetuser(pname) -> None:
    print(f"Hello, {pname}!")
    return None

def main() -> None:
    print("Program starting.")
    name = askName()
    greetuser(name)
    print("Program ending.")
    return None

main()