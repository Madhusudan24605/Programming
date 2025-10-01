print("Program starting.\n")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    celsius = float(input("Insert the amount of Celsius: "))
    fahrenheit = round((celsius * 1.8) + 32, 1)
    print(f"{celsius} °C equals to {fahrenheit} °F \n")

elif choice == 2:
    fahrenheit_val = float(input("Insert the amount of Fahrenheit: "))
    celsius_val = round((fahrenheit_val - 32) / 1.8, 1)
    print(f"{fahrenheit_val} °F equals to {celsius_val} °C \n")

elif choice == 0:
    print("Exiting...\n")

else:
    print("Unknown option.\n")

print("Program ending.")
