print("Program starting.")
print("This program analyses a list of names from a file.")

filename = input("Insert filename to read: ")

print(f'Reading names from "{filename}".')

names = []


with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        name = line.strip()
        if name != "":      
            names.append(name)

print("Analysing names...")


count = len(names)
shortest = min(len(n) for n in names)
longest = max(len(n) for n in names)
average = sum(len(n) for n in names) / count

print("Analysis complete!")


print("#### REPORT BEGIN ####")
print(f"Name count - {count}")
print(f"Shortest name - {shortest} chars")
print(f"Longest name - {longest} chars")
print(f"Average name - {average:.2f} chars")
print("#### REPORT END ####")

print("Program ending.")
