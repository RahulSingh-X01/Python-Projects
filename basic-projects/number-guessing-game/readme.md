# 🎲 Number Guessing Game

A fun command-line number guessing game where you try to guess a random number between 1 and 100 with limited attempts!

## 📖 About

This is an interactive guessing game where the computer picks a random number, and you have to guess it within a limited number of attempts. Choose your difficulty level and test your luck!

## 🎮 Game Rules

- The computer selects a random number between 1 and 100
- You choose a difficulty level:
  - **Easy Mode**: 10 attempts to guess the number
  - **Hard Mode**: 5 attempts to guess the number
- After each guess, you'll get a hint:
  - "Too high" if your guess is above the number
  - "Too low" if your guess is below the number
  - "You got it!" if you guess correctly
- Win by guessing the correct number before running out of attempts!

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `guessing_game.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the game:

```bash
python guessing_game.py
```

## 💻 Example Gameplay

### Easy Mode - Winning
```
Welcome to the Number Guessing Game!
I'm thinking of a number between '1' and '100'!
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts left to guess the number.
Make a guess : 50
Too low.
You have 9 attempts left to guess the number.
Make a guess : 75
Too high.
You have 8 attempts left to guess the number.
Make a guess : 63
You got it! The answer was 63
```

### Hard Mode - Losing
```
Welcome to the Number Guessing Game!
I'm thinking of a number between '1' and '100'!
Choose a difficulty. Type 'easy' or 'hard': hard
You have 5 attempts left to guess the number.
Make a guess : 50
Too low.
You have 4 attempts left to guess the number.
Make a guess : 75
Too high.
You have 3 attempts left to guess the number.
Make a guess : 60
Too low.
You have 2 attempts left to guess the number.
Make a guess : 70
Too high.
You have 1 attempts left to guess the number.
Make a guess : 65
Too low.
You've run out of guesses!
```

## ✨ Features

- **Two Difficulty Levels**: Choose between easy (10 attempts) or hard (5 attempts)
- **Helpful Hints**: Get feedback after each guess
- **Countdown Display**: See how many attempts you have left
- **Random Number Generation**: Every game is different
- **Clear Win/Loss Conditions**: Know exactly when the game ends

## 📋 Requirements

- Python 3.x
- No external libraries required (uses only standard library)

## 🎯 Strategy Tips

1. **Use Binary Search**: Start with 50, then adjust by halves
2. **Remember Your Hints**: Keep track of your high and low boundaries
3. **Stay Calm**: Don't waste guesses on random numbers
4. **Calculate Range**: Narrow down the possibilities with each guess

Example strategy:
- Guess 50 → Too low
- Now you know it's between 51-100
- Guess 75 → Too high
- Now you know it's between 51-74
- Continue halving the range!

## 🔮 Future Enhancements

Potential improvements for future versions:
- Add a replay option without restarting the program
- Track and display best scores (fewest guesses)
- Add a custom difficulty mode (user chooses number of attempts)
- Implement different number ranges (1-50, 1-1000, etc.)
- Add a hint system (costs an attempt)
- Show guess history during the game
- Add a timer for speed challenges
- Create a leaderboard system
- Add multiplayer mode

## 🛠️ Technical Details

- Uses Python's `random` module for number generation
- Implements `for-else` loop structure (else executes if loop completes without break)
- Range countdown using `range(n, 0, -1)` for attempts display
- Global variable to share the random number between functions

## 🎓 Learning Concepts

This project demonstrates:
- Random number generation
- User input handling
- Conditional statements (if/elif/else)
- For loops with else clause
- Function definitions
- Global variables
- String formatting

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

---

**Good Luck Guessing! 🍀**
