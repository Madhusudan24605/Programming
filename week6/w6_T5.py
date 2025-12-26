def readValues(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    numbers = []
    for line in lines:
        line = line.strip()
        if line != "":
            number = int(line)
            numbers.append(number)
    return numbers


def analyseValues(values):
    count = 0
    total = 0
    greatest = 0

    for num in values:
        count = count + 1
        total = total + num
        if num > greatest:
            greatest = num

    if count > 0:
        average = total / count
    else:
        average = 0

    result = "Count;Sum;Greatest;Average\n"
    result = result + f"{count};{total};{greatest};{average:.2f}\n"
    return result


if __name__ == "__main__":
    print("Program starting.")
    file_name = input("Insert filename:")
    print("#### Number analysis - START ####")
    print(f"File {file_name} results:")

    values = readValues(file_name)
    print(analyseValues(values), end="")

    print("#### Number analysis - END ####")
    print("Program ending.")