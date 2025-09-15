import random
round = 1
comp_wins = 0
player_wins = 0
while round < 6:
    print(f"ROUND {round}")
    
    player_input = str(input(f"Enter choice: ")).strip().lower()
    if player_input == "r" or player_input == "p" or player_input == "s":
        print(f"Good choice!")
    else:
        print("Invalid input!")
        while player_input != "r" or player_input != "p" or player_input != "s":
            player_input = str(input(f"Enter choice: ")).strip().lower()
            print(player_input)
            if player_input == "r" or player_input == "p" or player_input == "s":
                print(f"Good choice!")
                break
            else:
                print("Invalid input!")


    if player_input == "r":
        player_choice = "Rock"
    elif player_input == "p":
        player_choice = "Paper"
    else:
        player_choice = "Scissors"

    print(f"You picked... {player_choice}")

    comp_moves = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(comp_moves)

    print(f"The computer chose... \n... \n... \n{computer_choice}!")

    if player_choice == computer_choice:
        result = "Tied!"
    elif player_choice == "Rock" and computer_choice == "Scissors" or player_choice == "Paper" and computer_choice == "Rock" or player_choice == "Scissors" and computer_choice == "Paper":
        result = "You won!"
        player_wins += 1
    else:
        result = "You lost... Tough luck!"
        comp_wins += 1
    print(f"{result}\n")

    round += 1

print("The series has ended!")
print(f"You won\n...\n{player_wins} rounds!")
print(f"\nThe computer won\n...\n{comp_wins} rounds!\n")
print(f"The judges have declared...\n...\n...")
if player_wins == comp_wins:
    print("A tie!")
elif player_wins > comp_wins:
    print("You win!")
else:
    print("The computer wins!")