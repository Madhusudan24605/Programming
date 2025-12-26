

print("Program starting.")


class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0



def readTimestamps(filename, timestamps):
    with open(filename, "r") as f:
        lines = f.readlines()
        data_lines = lines[1:]  

    for line in data_lines:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(";")
        t = TIMESTAMP()
        t.weekday = parts[0]
        t.hour = parts[1]
        t.consumption = float(parts[2])
        t.price = float(parts[3])
        timestamps.append(t)



def displayTimestamps(timestamps):
    print("Electricity usage:")
    for t in timestamps:
        total = t.price * t.consumption
        print(f" - {t.weekday} {t.hour}, price {t.price:.2f} €, consumption {t.consumption:.2f} kWh, total {total:.2f} €")



def main():
    file_name = input("Insert filename: ")
    print(f'Reading file "{file_name}".')
    timestamps = []
    readTimestamps(file_name, timestamps)
    displayTimestamps(timestamps)
    print("Program ending.")


if __name__ == "__main__":
    main()