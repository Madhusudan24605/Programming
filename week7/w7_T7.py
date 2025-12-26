ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def load_config(filename: str) -> tuple[list[str], str]:
    rotors: list[str] = ["", "", ""]
    reflector = ""

    print(f"Insert config(filename): {filename}")  

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                key, value = line.split(":", 1)
                value = value.strip()
                if key == "Rotor1":
                    rotors[0] = value
                elif key == "Rotor2":
                    rotors[1] = value
                elif key == "Rotor3":
                    rotors[2] = value
                elif key == "Reflector":
                    reflector = value
    except FileNotFoundError:
        print("Error: configuration file not found.")
        return [], ""

    return rotors, reflector


def step_rotors(positions: list[int]) -> None:
    
    positions[0] = (positions[0] + 1) % 26
    
    if positions[0] == 0:
        positions[1] = (positions[1] + 1) % 26
        if positions[1] == 0:
            positions[2] = (positions[2] + 1) % 26


def rotor_forward(ch: str, wiring: str, pos: int) -> str:
    
    idx_in = ALPHABET.index(ch)
    shifted_in = (idx_in + pos) % 26
    wired_letter = wiring[shifted_in]
    idx_out = ALPHABET.index(wired_letter)
    shifted_out = (idx_out - pos) % 26
    return ALPHABET[shifted_out]


def rotor_reverse(ch: str, wiring: str, pos: int) -> str:
    
    idx_in = ALPHABET.index(ch)
    shifted_in = (idx_in + pos) % 26
    letter_at_contact = ALPHABET[shifted_in]
    
    wired_index = wiring.index(letter_at_contact)
    shifted_out = (wired_index - pos) % 26
    return ALPHABET[shifted_out]


def reflect(ch: str, reflector: str) -> str:
    idx = ALPHABET.index(ch)
    return reflector[idx]


def encode_char(
    ch: str,
    rotors: list[str],
    reflector: str,
    positions: list[int],
) -> str:
    
    step_rotors(positions)

    
    c = ch
    c = rotor_forward(c, rotors[0], positions[0])
    c = rotor_forward(c, rotors[1], positions[1])
    c = rotor_forward(c, rotors[2], positions[2])

    
    c = reflect(c, reflector)

    
    c = rotor_reverse(c, rotors[2], positions[2])
    c = rotor_reverse(c, rotors[1], positions[1])
    c = rotor_reverse(c, rotors[0], positions[0])

    return c


def main() -> None:
    
    config_filename = input("Insert config(filename): ")
    rotors, reflector = load_config(config_filename)

    if not rotors or not reflector:
        print("Enigma closing.")
        return

    
    plug_answer = input("Insert plugs (y/n)?: ")
    if plug_answer.lower() == "y":
        print("Plugboard feature not implemented.")
    else:
        print("No extra plugs inserted.")

    print("Enigma initialized.\n")

    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            print("\nEnigma closing.")
            break

        positions = [0, 0, 0]  

        converted_chars: list[str] = []

        for ch in row:
            if ch.upper() in ALPHABET:
                original = ch.upper()
                illuminated = encode_char(original, rotors, reflector, positions)
                print(f'Character "{original}" illuminated as "{illuminated}"')
                converted_chars.append(illuminated)
            else:
                
                converted_chars.append(ch)

        converted_row = "".join(converted_chars)
        print(f'Converted row - "{converted_row}".\n')


if __name__ == "__main__":
    main()
