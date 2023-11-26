import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
while True:
    play_again = input("Do you want to play? (yes/no): ").lower()
    if play_again != 'yes':
        break
    rock_paper_scissors()
