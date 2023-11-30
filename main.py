import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper and scissors): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices =  {"player": player_choice, "computer": computer_choice}
    return choices
    
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if  player == computer:
        return "It is a tie!"
    elif player == "rock": 
        if computer == "scissor":
            return "Rock smashes scissors! You win."
        else:
            return "Paper covers rock! You lose."
    elif player == "paper": 
        if computer == "rock":
            return "Paper covers rock! You win."
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissor": 
        if computer == "rock":
            return "Rock breaks scissors! You lose."
        else:
            return "Scissors cuts paper! You win."
