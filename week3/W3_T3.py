print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

user_name=input("Before the menu, please insert your name: ")

print("\nOptions: ")
print("1 - Print welcome message \n0 - Exit ")

menu_choice=int(input("Your choice: "))
if menu_choice==1:
 print(f"Welcome {user_name}! \n")
elif menu_choice==0:
 print(f"Exiting ...\n")
else:
 print("Unknown option. \n")

print("Program ending.")