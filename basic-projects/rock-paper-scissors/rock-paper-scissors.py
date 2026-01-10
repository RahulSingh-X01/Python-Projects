import random

user_choice = int(
    input("What do you want to choose?\nType 0 for rock, 1 for paper, 2 for scissors:\n")
)

if user_choice not in [0, 1, 2]:
    print("You typed an invalid input. You lose.")
else:
    print(f"Your choice: {user_choice}")

    computer_choice = random.randint(0, 2)
    print(f"Computer's choice: {computer_choice}")

    if user_choice == 0 and computer_choice == 2:
        print("You win.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif computer_choice == user_choice:
        print("It's a draw.")
    elif user_choice > computer_choice:
        print("You win.")
    else:
        print("You lose.")