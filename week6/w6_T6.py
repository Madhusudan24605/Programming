LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(ch, alphabet):
    
    if ch in alphabet:
        pos = alphabet.index(ch)
        new_pos = (pos + 13) % 26
        return alphabet[new_pos]
    else:
        return ch


def rot13(text):
    
    result = ""
    for ch in text:
        if ch in LOWER_ALPHABETS:
            result = result + shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch in UPPER_ALPHABETS:
            result = result + shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result = result + ch
    return result


def writeFile(filename, content):
    
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(content)


if __name__ == "__main__":
    print("Program starting.")
    file_name = input("Insert output filename: ")
    text = input("Insert text to encode with ROT13: ")

    encoded_text = rot13(text)
    writeFile(file_name, encoded_text)

    print("ROT13 encoded text written to file:", file_name)
    print("Program ending.")