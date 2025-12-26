
def askPositiveInteger() -> int:
    Feed = input("Insert positive integer(negative stops): ")
    try:
        value = int(Feed)
        return value
    except ValueError:
        return 0   


def displayIntegers(integers: list[int]) -> None:
    if len(integers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(integers)} integers:")
        for index, value in enumerate(integers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")
    return None


def main():
    print("Program starting.")
    print("Collect positive integers.")

    positive_integers: list[int] = []

    while True:
        number = askPositiveInteger()

        if number < 0:
            break
        elif number > 0:
            positive_integers.append(number)
        

    print("Stopped collecting positive integers.")
    displayIntegers(positive_integers)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()






