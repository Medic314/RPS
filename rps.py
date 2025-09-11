import random
input = str(input(f"Enter choice: ")).strip().lower()
if input == "r" or input == "p" or input == "s":
    print(f"Good choice!")
else:
    print("Invalid input!")
    exit()

if input == "r":
    player_choice = "Rock"
elif input == "p":
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
else:
    result = "You lost... Tough luck!"
print(result)