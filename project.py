import random 

print("WELCOME to Rock-Paper-Scissors!")

def  play():

    # Players Choice
    options = ["rock", "paper", "scissors"]
    user_choice = input("Choose: rock, paper, or scissors:\n").lower()

    #Computer Choice
    computer_choice = random.choice(options).lower()


    print("You chose: " + user_choice)
    print("Computer chose: " + computer_choice)

    #Compare choices and determine winner!
    if user_choice == computer_choice:
        print("It's a tie!")    
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")


def main():
    play()
    while True:
        play_again = input("Do you want to play again yes/no?\n").lower()
        if play_again == "yes": 
            play()
        else:
            break 
main()
