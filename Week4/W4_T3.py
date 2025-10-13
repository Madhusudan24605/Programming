print("Program starting.\n")
value1 = int(input("Insert starting value: "))
value2 = int(input("Insert stopping value: "))
print("\nStarting while-loop:")
i = value1
while i!= value2 + 1:
    if(i==value2):
        print(i)
    else:
        print(i, end=' ')
    i += 1
print("\nProgram ending.")