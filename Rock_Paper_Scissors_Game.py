import random

def get_computer_choice():
    return random.choice([1, 2, 3])

def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("1: Rock\n2: Paper\n3: Scissors")

    while True:
        try:
            user_choice = int(input("Enter your choice (1-3): "))
            if user_choice not in [1, 2, 3]:
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou chose {get_choice_name(user_choice)}")
        print(f"Computer chose {get_choice_name(computer_choice)}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
