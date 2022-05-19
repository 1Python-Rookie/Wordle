import random
import time
print("This is my rock, paper, scissors game. \n Type an option then press 'Enter'")
choices = ["Rock", "Paper", "Scissors"]
player_points = 0
cpu_points = 0
for index in range(1, 6):
    computer = random.choice(choices)
    while True:
        player = input("Rock, Paper or Scissors? ")
        if not player.upper() == "ROCK" and not player.upper() == "PAPER" and not player.upper() == "SCISSORS":
            print("Enter one of the following choices")
            print("Either rock, paper or scissors stupid!!")
            continue
        else:
            break
    print("You chose: " + player.capitalize())
    print("Computer chose: " + computer)
    time.sleep(2)
    if computer.upper() == "ROCK" and player.upper() == "SCISSORS":
        print("Computer won this round")
        cpu_points = cpu_points + 1
        print(cpu_points)
        print(player_points)
    elif computer.upper() == "PAPER" and player.upper() == "ROCK":
        print("Computer won this round")
        cpu_points = cpu_points + 1
        print(cpu_points)
        print(player_points)
    elif computer.upper() == "SCISSORS" and player.upper() == "PAPER":
        print("Computer won this round")
        cpu_points = cpu_points + 1
        print(cpu_points)
        print(player_points)
    elif computer.upper() == "SCISSORS" and player.upper() == "ROCK":
        print("You won this round!")
        player_points = player_points + 1
        print(cpu_points)
        print(player_points)
    elif computer.upper() == "ROCK" and player.upper() == "PAPER":
        print("You won this round!")
        player_points = player_points + 1
        print(cpu_points)
        print(player_points)
    elif computer.upper() == "PAPER" and player.upper() == "SCISSORS":
        print("You won this round!")
        player_points = player_points + 1
        print(cpu_points)
        print(player_points)
    else:
        print("Tie! No points")
        print(cpu_points)
        print(player_points)
if player_points > cpu_points:
    print("Congrats! You won!")
elif cpu_points > player_points:
    print("The computer won. Better luck next time")
else:
    print("Woah you tied with the computer!")
