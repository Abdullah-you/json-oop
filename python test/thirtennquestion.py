import random

def npc_choice():
    npc = random.choices(["rock","paper","scissors"], weights=[1,1,1], k=1)
    return npc[0]

def game():
    user_choice = input("Enter your choice: ").lower()
    computer_choice = npc_choice()
    print(f"computer choose: {computer_choice}")
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("You lost!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lost!")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lost!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
    else:
        print("Invalid choice!")
        
if __name__ == '__main__':
    while True:
        game()
        play_again = input("Play Again..? Press 'Y' for Yes or 'N' for No: " )
        if play_again.lower() == "y":
            continue
        elif play_again.lower() == "n":
            break









