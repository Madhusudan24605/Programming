print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

user_name = input("Before the menu, please insert your name: ")

print("Options: ")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

name_reversed = user_name[::-1]
name_length = len(user_name)
first_char = user_name[0]

option_choice = int(input("Your choice: "))

if option_choice == 1:
    print(f"Welcome {user_name}! \n")
elif option_choice == 2:
    print(f'Your name backwards is "{name_reversed}" \n')
elif option_choice == 3:
    print(f'The first character in name "{user_name}" is "{first_char}" \n')
elif option_choice == 4:
    print(f'There are {name_length} characters in the name "{user_name}"')
    print(f'"{user_name}" \n')
elif option_choice == 0:
    print("Exiting ...\n")
else:
    print("Unknown option. \n")

print("Program ending.")
