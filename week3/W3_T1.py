print("program starting. \nInsert two integers.")
feed1 = int(input("Insert first integer: "))
feed2 = int(input("Insert second integer: "))
print ("compare inserted integers.")
if feed1 > feed2:
    print("First integer is greater.")
elif feed2 > feed1:
    print("Second integer is greater.")
else:
    print("Integers are the same")
print("")
print("adding integers together")
sum = feed1+ feed2
print("checking the party of the sum..")
Remender = sum % 2
if Remender == 0:
    print("sum is even.")
else:
    print("sum is odd.")
print("program ending.")

   