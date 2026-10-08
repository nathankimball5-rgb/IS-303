# Import random and set up variables
import random
computer_answers = ["rock", "paper", "scissors"]
losses = 0
wins = 0

# the following function gets the user choice and returns that choice
def get_player_choice():
    user_input = input("Enter rock, paper, scissors: ")
    user_input = user_input.lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print(f"Sorry {user_input} is not a valid choice. Please try again.")
        user_input = input("Enter rock, paper, scissors: ")
        user_input = user_input.lower()
    return user_input

# The following function determines and returns whether it is a tie, loss, or win
def determine_winner(computer_choice, user_input):
    if computer_choice == user_input:
        return "tie"
    elif (computer_choice == "rock" and user_input == "scissors") or (computer_choice == "scissors" and user_input == "paper") or (computer_choice == "paper" and user_input == "rock"):
        return "loss"
    else:
        return "win"

# Welcome user to the game and get the input, make sure that the number of rounds is odd. 
print("Welcome to Rock Paper Scissors")
number_of_rounds = int(input("How many rounds would you like to play:"))
while number_of_rounds % 2 != 1:
    print("Please enter an odd number of rounds.")
    number_of_rounds = int(input("Please try again: "))


# Runs the game calling the appropriate functions when needed. If tie, play again. 
# Tell user if they won or lost and add up times won or lost. 
for i in range(number_of_rounds):
    user_input = get_player_choice()
    computer_choice = random.choice(computer_answers)
    print(f"The computer chose {computer_choice}.")
    result = determine_winner(computer_choice, user_input)
    while result == "tie":
        print("Tie! Play again.")
        user_input = get_player_choice()
        computer_choice = random.choice(computer_answers)
        print(f"The computer chose {computer_choice}.")
        result = determine_winner(computer_choice, user_input)

    if result == "loss":
        print("You lost.")
        losses += 1
    elif result == "win":
        print("You win!")
        wins += 1

# print the final part telling user if they won or lost and the scores between user and computer.
print("---------------------------")
print(f"Score-You: {wins} | Computer: {losses}")
if wins > losses:
    print("You win!!!")
elif wins < losses:
    print("You lose!")
print("Thanks for playing!")

