print("program starting.")
print("String comparisons")
feed1 = input("Insert first word: ")
character = input("Insert a character: ")
if (character in feed1):
    print(f"word \"{feed1}\" contains character \"{character}\"")
else:
    print(f"word \"{feed1}\" does not contain character \"{character}\"")
feed2 = input("Insert second word: ")
if (feed2 > feed1):
    print(f"The first word \"{feed1}\" is before the second word \"{feed2}\" in the alphabetically.")
elif (feed1 < feed2):
    print(f"The second word \"{feed2}\" is before the first word \"{feed1}\" in the alphabetically.")

print("program ending.")