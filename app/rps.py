# Rock Paper Scissors Game

import random
VALID_OPTIONS = ['rock','paper','Scissors']

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        result = "TIE GAME"
    elif (player_choice == 'rock' and computer_choice == 'Scissors'):
        result = "USER WIN"
    elif (player_choice == 'rock' and computer_choice == 'paper'):
        result = "COMP WIN"
    elif (player_choice == 'Scissors' and computer_choice == 'rock'):
        result = "COMP WIN"
    elif (player_choice == 'Scissors' and computer_choice == 'paper'):
        result = "USER WIN"
    elif (player_choice == 'paper' and computer_choice == 'Scissors'):
        result = "COMP WIN"
    elif (player_choice == 'paper' and computer_choice == 'rock'):
        result = "USER WIN"
    return (result)

def generate_random_choice():
    return random.choice(VALID_OPTIONS)

# only run code indented inside 
# if we are running this script from the command line
# but not if we are importing
if __name__ == "__main__":
    print("Welcome to the game!")

    player_choice = input(f"Select an option {VALID_OPTIONS}:")
    print("user choice:", player_choice)

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMPUTER CHOOSES:", computer_choice)

    print(determine_winner(player_choice, computer_choice))

