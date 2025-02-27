import random 
Choices=["paper","rock","scissor"]

player_1=input("Enter rock, paper, or scissors: ")
if player_1 not in Choices:
    print("Invalid input. Please enter rock, paper, or scissors.")
else:
    player_2=random.choice(Choices)
    print("player_2", player_2)
    
    if player_1==player_2:
        print("It's a tie!")
    elif ( player_1== 'rock' and player_2 == 'scissors') or \
         (player_1 == 'paper' and player_2 == 'rock') or \
         (player_1 == 'scissors' and player_2 == 'paper'):
        print("You win!")
    else:
        print("You lose!")

