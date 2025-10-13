print("Program starting.\n")
value1 = int(input("Insert starting value: "))
value2 = int(input("Insert stopping value: "))
print("\nStarting for-loop:")
if value1 < value2:
    for i in range(value1, value2 + 1):
     print(i, end=' ')
print("\nProgram ending.")