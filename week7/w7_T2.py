def main() -> None:
    print("Program starting.")

    user_input = input("Insert comma separated integers: ")

    parts = user_input.split(",")
    valid_integers: list[int] = []

    for part in parts:
        value = part.strip()
        try:
            number = int(value)
            valid_integers.append(number)
        except ValueError:
            print(f"Error: '{value}' is not a valid integer.")

    if len(valid_integers) == 0:
        print("No valid integers to analyze.")
        print("Program ending.")
        return

    total = sum(valid_integers)
    count = len(valid_integers)
    parity = "even" if total % 2 == 0 else "odd"

    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {total} and it's {parity}")
    print("Program ending.")


if __name__ == "__main__":
    main()
