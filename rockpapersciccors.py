import random

while True:
    my_input = input("Enter a choice (rock, paper, scissors): ")
    if my_input=="quit":
        break
    computer_input= random.choice(["rock", "paper", "scissors"])
    print(f"computer chose {computer_input}.\n")
    if my_input == computer_input:
        print(f"Both players selected {my_input}. It's a tie!")
    elif my_input == "rock":
        print("You win!")if computer_input == "scissors" else print("You lose.")
    elif my_input== "paper":
        print("You win!")if computer_input == "rock" else print("You lose.")        
    elif my_input == "scissors":
       print("You win!") if computer_input == "paper" else print("You lose.")

