import os

def rot13(text: str) -> str:
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)



def load_progress():
    if not os.path.exists("player_progress.txt"):
        with open("player_progress.txt", "w", encoding="utf-8") as f:
            f.write("current_location;next_location;passphrase\n")
            f.write("0;1;qvfpvcyvar\n")  
        return 0, 1, "qvfpvcyvar"

    with open("player_progress.txt", "r", encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    last = lines[-1]
    parts = last.split(";")
    return int(parts[0]), int(parts[1]), parts[2]


def save_progress(current, nxt, passphrase):
    with open("player_progress.txt", "a", encoding="utf-8") as f:
        f.write(f"{current};{nxt};{passphrase}\n")



def main():
    place_names = [
        "home",
        "Galba's palace",
        "Otho's palace",
        "Vitellius' palace",
        "Vespasian's palace"
    ]

    print("Travel starting.")

    current, nxt, cipher_pass = load_progress()

    print(f"Currently at {place_names[current]}.")
    print(f"Travelling to {place_names[nxt]}...")
    print(f"...Arriving to the {place_names[nxt]}.")


    plain_pass = rot13(cipher_pass)
    print("Passing the guard at the entrance.")
    print(f"\"{plain_pass.capitalize()}!\"")


    print("Looking for the message in the palace...")
    filename = f"{nxt}_{cipher_pass}.gkg"

    if not os.path.exists(filename):
        print("Message file missing!")
        print("Travel ending.")
        return

    print("Ah, there it is! Seems cryptic.")

    with open(filename, "r", encoding="utf-8") as f:
        cipher_line = f.readline().rstrip()

    
    save_progress(nxt, nxt + 1 if nxt + 1 < len(place_names) else nxt, cipher_pass)
    print("[Game] Progress autosaved!")

    
    print("Deciphering Emperor's message...")
    plain_line = rot13(cipher_line)

    
    outname = f"{nxt}-{plain_pass}.txt"
    with open(outname, "w", encoding="utf-8") as f:
        f.write(plain_line + "\n")

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")


if __name__ == "__main__":
    main()
