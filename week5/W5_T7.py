DELIMITER = ','
def collectWords() -> str:
    words = ""
    while True:
        word = input("Insert word(empty stops): ")
        WordCount = 0
        CharCount = 0
        if word == "":
            break
        if words != "":
            words = words + DELIMITER + word
        else:
            words = word
    return str(words)

def analyseWords(words):
    if words == "":
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return None
    else:
        WordCount = words .count(DELIMITER) + 1
        CharCount = len(words) - words.count(DELIMITER)
        Avg = CharCount / WordCount
        print (f"- {WordCount} Words.")
        print (f"- {CharCount} Characters.")
        print ("- {:.2f} Average word length.".format(Avg))
        return None

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print ("Program ending.")
    return None
main()