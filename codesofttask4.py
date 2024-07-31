import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"


def play_round():
    choices = ['rock', 'paper', 'scissors']

    
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in choices:
            break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

    
    computer_choice = random.choice(choices)

    
    result = determine_winner(user_choice, computer_choice)

    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

    return result


def main():
    print("Welcome to Rock-Paper-Scissors!")

    user_score = 0
    computer_score = 0

    while True:
        result = play_round()

        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing Rock-Paper-Scissors!")
            break

    print("Final Score:")
    print(f"You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()
