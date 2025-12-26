import random
random.seed(1234)

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def get_ascii(choice: int) -> str:
    if choice == 1:
        return ROCK
    elif choice == 2:
        return PAPER
    else:
        return SCISSORS


def choice_to_word(choice: int) -> str:
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"


def determine_winner(player: int, bot: int) -> str:
    if player == bot:
        return "draw"

    if player == 1 and bot == 3:
        return "player"
    if player == 2 and bot == 1:
        return "player"
    if player == 3 and bot == 2:
        return "player"

    return "bot"


def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")

    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    player_wins = 0
    player_losses = 0
    player_draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")

        choice_input = input("Your choice: ")

        try:
            player_choice = int(choice_input)
        except ValueError:
            continue

        if player_choice == 0:
            break

        if player_choice not in (1, 2, 3):
            continue

        bot_choice = random.randint(1, 3)

        print("Rock! Paper! Scissors! Shoot!\n")

        print("#########################")
        print(f"{player_name} chose {choice_to_word(player_choice)}.\n")
        print(get_ascii(player_choice))
        print("#########################")

        print(f"RPS-3PO chose {choice_to_word(bot_choice)}.\n")
        print(get_ascii(bot_choice))
        print("#########################\n")

        result = determine_winner(player_choice, bot_choice)

        if result == "draw":
            print(f"Draw! Both players chose {choice_to_word(player_choice)}.\n")
            player_draws += 1
        elif result == "player":
            print(f"{player_name} {choice_to_word(player_choice)} beats RPS-3PO {choice_to_word(bot_choice)}.\n")
            player_wins += 1
        else:
            print(f"RPS-3PO {choice_to_word(bot_choice)} beats {player_name} {choice_to_word(player_choice)}.\n")
            player_losses += 1

    print("\nResults:")
    print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})")
    print(f"RPS-3PO - wins ({player_losses}), losses ({player_wins}), draws ({player_draws})\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
