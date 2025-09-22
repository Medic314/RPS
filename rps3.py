import random
def main():
    round = 1
    comp_wins = 0
    player_wins = 0
    for num in range(1, 6):
        print(f"ROUND {round}")
        
        player_input = get_valid_input()
        player_input = convert_letter_to_word(player_input)

        print(f"You picked... {player_input}")

        comp_moves = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(comp_moves)
        print(f"The computer chose... \n... \n... \n{computer_choice}!")
        outcome = determine_outcome(player_input, computer_choice)
        print_round_result(outcome)
        if outcome == "won":
            player_wins += 1
        elif outcome == "lost":
            comp_wins += 1


        round += 1
    print_series_results(player_wins, comp_wins)



def get_valid_input():
    """Loops until valid input is given, either r, p, or s"""
    player_input = str(input(f"Enter choice: ")).strip().lower()
    if player_input == "r" or player_input == "p" or player_input == "s":
        print(f"Good choice!")
        return player_input
    else:
        print("Invalid input!")
        while player_input != "r" or player_input != "p" or player_input != "s":
            player_input = str(input(f"Enter choice: ")).strip().lower()
            print(player_input)
            if player_input == "r" or player_input == "p" or player_input == "s":
                print(f"Good choice!")
                return player_input
            else:
                print("Invalid input!")

def determine_outcome(user, comp):
    """determines the outcome of the match, and returns it in a string"""
    if user == comp:

        return "tied"
    elif user == "Rock" and comp == "Scissors" or user == "Paper" and comp == "Rock" or user == "Scissors" and comp == "Paper":
        return "won"
    else:
        return "lost"

def convert_letter_to_word(letter):
    """converts the one-lettered input from the player into a proper, capitalized choice of rock, paper, or scissors"""
    if letter == "r":
        return "Rock"
    elif letter == "p":
        return "Paper"
    else:
        return "Scissors"
    
def print_round_result(result):
    """prints the round result"""
    if result == "lost":
        print(f"You lost... Tough luck!\n")
    elif result == "won":
        print(f"You won!\n")
    else:
        print(f"Tied!\n")
    

def print_series_results(user_wins, computer_wins):
    """determines and prints the final results of the whole series"""
    print("The series has ended!")
    print(f"You won\n...\n{user_wins} rounds!")
    print(f"\nThe computer won\n...\n{computer_wins} rounds!\n")
    print(f"The judges have declared...\n...\n...")
    if user_wins == computer_wins:
        print("A tie!")
    elif user_wins > computer_wins:
        print("You win!")
    else:
        print("The computer wins!")



if __name__ == "__main__":
    main()