# Rock Paper Scissors Game

print("Welcome to the game!")

player_choice = input("Select an option:")
print("user choice:", player_choice)

import random

VALID_OPTIONS = ['Rock','Paper','Scissor']

computer_choice = random.choice(VALID_OPTIONS)
print("comp choice:", computer_choice)

print("Winner: To Do")
