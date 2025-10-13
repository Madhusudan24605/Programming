print("Program starting.\n")
Wordcount = 0
charcount = 0
word = input("Insert a word (empty stops): ")
while word != "":
    Wordcount += 1
    charcount += len(word)
    word = input("Insert a word (empty stops): ")

print("\nYou inserted:")
print(f"- {Wordcount} words")
print(f"- {charcount} characters")

print("\nProgram ending.")
