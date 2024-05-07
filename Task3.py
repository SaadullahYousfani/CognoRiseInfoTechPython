#Rock Paper Scissors 

import random 

def get_user_input():
    while True:
        print("Rock Paper Scissors: ")
        user_choice = input("User Move: ").strip().lower()
        if user_choice in ['rock','paper','scissors']:
            return user_choice
        else:
            print("Invalid Choice. Please choose rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Same Move. It's a Draw"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You Win"  
    else:
        return "CPU Wins"
     
def play_the_game():
    user_score = 0
    cpu_score = 0

    while True:
        print("\n Lets Play The Game Rock, Papers, Scissors")
        user_selection = get_user_input()
        cpu_selection = get_computer_choice()
        print(f"\nYour Move: {user_selection}")
        print(f"Computer's move: {cpu_selection}")
        result = determine_winner(user_selection, cpu_selection)
        print(result)

        if 'You Win' in result:
            user_score += 1
        elif 'CPU Wins' in result:
            cpu_score += 1

        print(f"\n Your Score: {user_score} | Computer's Score: {cpu_score}")  
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThank you for playing!")
            break

play_the_game()
