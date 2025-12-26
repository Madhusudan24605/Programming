print("Program starting.")
print("This program can read a file.")

filename = input("Insert filename: ")

try:
    with open(filename, "r") as f:
        print(f'#### START "{filename}" ####')
        for line in f:
            print(line.rstrip())
        print(f'#### END "{filename}" ####')
except FileNotFoundError:
    print(f'Error: File "{filename}" not found.')

print("Program ending.")
