import random

# Function to display game rules
def display_rules():
    print("Welcome to Rock-Paper-Scissors!")
    print("The rules are simple:")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()

# Function to get user's choice
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

# Function to get computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

# Function to display the result of a single round
def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

# Function to play a single round
def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    return winner

# Function to play multiple rounds
def play_game():
    display_rules()
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))
    for _ in range(rounds):
        winner = play_round()
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        print(f"Score: You {user_score} - {computer_score} Computer")
        print()
    
    print("Game Over!")
    if user_score > computer_score:
        print(f"You won the game with a score of {user_score} to {computer_score}!")
    elif computer_score > user_score:
        print(f"Computer won the game with a score of {computer_score} to {user_score}!")
    else:
        print("The game ended in a tie!")

# Main function to start the game
def main():
    play_game()

if __name__ == "__main__":
    main()


