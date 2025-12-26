WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))

    PRows.clear()

    try:
        filehandle = open(PFilename, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Error: File not found.")
        return

    first = True
    for line in filehandle:
        if first:
            first = False
            continue

        if line == "\n":
            continue

        PRows.append(line.strip())

    filehandle.close()
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")

    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]

    for row in PRows:
        for i in range(len(WEEKDAYS)):
            if row.startswith(WEEKDAYS[i]):
                WeekdayTimestampAmount[i] += 1

    PResults.append("### Timestamp analysis ###")
    for i in range(len(WEEKDAYS)):
        PResults.append(f" - {WEEKDAYS[i]} {WeekdayTimestampAmount[i]} stamps")
    PResults.append("### Timestamp analysis ###")

    WeekdayTimestampAmount.clear()
    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None


def main() -> None:
    print("Program starting.")

    Rows: list[str] = []
    Results: list[str] = []

    filename = input("Insert filename: ")

    readFile(filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)

    Rows.clear()
    Results.clear()

    print("Program ending.")
    return None


main()
