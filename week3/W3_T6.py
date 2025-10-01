print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below. \n")
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

menu_choice = int(input("Your choice: "))

if menu_choice == 2:
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    weight_choice = int(input("Your choice: "))
    if weight_choice == 2:
        pounds_input = float(input("Insert pounds: "))
        grams_output = round(pounds_input * 453.6, 1)
        print(f"{pounds_input} lb is {grams_output} g")
    elif weight_choice == 1:
        grams_input = float(input("Insert grams: "))
        pounds_output = round(grams_input / 453.6, 1)
        print(f"{grams_input} g is {pounds_output} lb")
    elif weight_choice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif menu_choice == 1:
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    length_choice = int(input("Your choice: "))
    if length_choice == 2:
        km_input = float(input("Insert kilometers: "))
        m_output = km_input * 1000
        print(f"{km_input} km is {m_output} m")
    elif length_choice == 1:
        m_input = float(input("Insert meters: "))
        km_output = m_input / 1000
        print(f"{m_input} m is {km_output} km")
    elif length_choice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif menu_choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
