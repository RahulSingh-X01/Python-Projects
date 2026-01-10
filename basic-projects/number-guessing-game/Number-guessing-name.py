import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between '1' and '100'!")
number = random.randint(1, 100)
# print(number)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def hard_level():
    global number
    for attempts in range(5, 0, -1):
        print(f"You have {attempts} attempts left to guess the number.")
        guess = int(input("Make a guess : "))
        if guess > number:
            print("Too high.")
        elif guess == number:
            print(f"You got it! The answer was {number} ")
            break
        else:
            print("Too low.")
    else:
        print("You've run out of guesses!")


def easy_level():
    global number
    for attempts in range(10, 0, -1):
        print(f"You have {attempts} attempts left to guess the number.")
        guess = int(input("Make a guess : "))
        if guess > number:
            print("Too high.")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            break
        else:
            print("Too low.")
    else:
        print("You've got run out of guesses!")


if difficulty == "hard":
    hard_level()
if difficulty == "easy":
    easy_level()