import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        try:
            user_choice = int(input("Enter your choice (1-4): "))
            if user_choice == 4:
                print("Thanks for playing! Final scores:")
                print(f"You: {user_score} | Computer: {computer_score}")
                break
            elif user_choice not in range(1, 4):
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue

            choices = ["rock", "paper", "scissors"]
            user_choice = choices[user_choice - 1]
            computer_choice = random.choice(choices)

            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if "win" in result:
                user_score += 1
            elif "lose" in result:
                computer_score += 1

            print(f"Scores - You: {user_score} | Computer: {computer_score}")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    rock_paper_scissors()
