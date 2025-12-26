DELIMITER = ";"


class TIMESTAMP:
    def __init__(self, weekday="", hour="", consumption=0.0, price=0.0):
        self.weekday = weekday
        self.hour = hour
        self.consumption = consumption
        self.price = price


def readTimestamps(filename, timestamps):
    with open(filename, "r") as f:
        lines = f.readlines()[1:]  

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(DELIMITER)

        t = TIMESTAMP(
            weekday=parts[0],
            hour=parts[1],
            consumption=float(parts[2]),
            price=float(parts[3])
        )

        timestamps.append(t)


def analyseTimestamps(timestamps):
    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturnday", "Sunday"
    ]

    summary = {day: {"cons": 0.0, "cost": 0.0} for day in days}

    for t in timestamps:
        if t.weekday in summary:
            summary[t.weekday]["cons"] += t.consumption
            summary[t.weekday]["cost"] += t.consumption * t.price

    return summary


def displayResults(summary):
    print("### Electricity consumption summary ###")
    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturnday", "Sunday"
    ]
    for day in days:
        values = summary[day]
        print(
            f" - {day} usage {values['cons']:.2f} kWh, "
            f"cost {values['cost']:.2f} €"
        )
    print("### Electricity consumption summary ###")


def main():
    print("Program starting.")
    filename = input()
    print(f'Reading file "{filename}".')

    timestamps = []
    readTimestamps(filename, timestamps)

    print("Analysing timestamps.")
    summary = analyseTimestamps(timestamps)

    print("Displaying results.")
    displayResults(summary)

    print("Program ending.")


if __name__ == "__main__":
    main()