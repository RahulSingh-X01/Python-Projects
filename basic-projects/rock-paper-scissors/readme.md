# ✊✋✌️ Rock Paper Scissors Game

A classic Rock, Paper, Scissors game where you compete against the computer in this timeless hand game!

## 📖 About

This is a digital version of the popular Rock, Paper, Scissors game. Make your choice and see if you can beat the computer's random selection. The game follows the traditional rules and provides instant results!

## 🎮 Game Rules

### How to Win
- **Rock (0) beats Scissors (2)** - Rock crushes scissors
- **Paper (1) beats Rock (0)** - Paper covers rock
- **Scissors (2) beats Paper (1)** - Scissors cut paper

### Outcomes
- **Win**: Your choice beats the computer's choice
- **Lose**: Computer's choice beats your choice
- **Draw**: Both choose the same option

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `rock_paper_scissors.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the game:

```bash
python rock_paper_scissors.py
```

## 💻 Example Gameplay

### Example 1: Player Wins
```
What do you want to choose?
Type 0 for rock, 1 for paper, 2 for scissors:
0
Your choice: 0
Computer's choice: 2
You win.
```

### Example 2: Player Loses
```
What do you want to choose?
Type 0 for rock, 1 for paper, 2 for scissors:
2
Your choice: 2
Computer's choice: 0
You lose.
```

### Example 3: Draw
```
What do you want to choose?
Type 0 for rock, 1 for paper, 2 for scissors:
1
Your choice: 1
Computer's choice: 1
It's a draw.
```

### Example 4: Invalid Input
```
What do you want to choose?
Type 0 for rock, 1 for paper, 2 for scissors:
5
You typed an invalid input. You lose.
```

## ✨ Features

- **Simple Input System**: Numbers 0, 1, 2 for easy selection
- **Random Computer Choice**: Unpredictable opponent
- **Input Validation**: Handles invalid inputs gracefully
- **Clear Output**: Shows both choices and the result
- **Fair Game**: Follows traditional Rock, Paper, Scissors rules

## 🎯 Input Guide

| Number | Choice |
|--------|--------|
| 0 | Rock ✊ |
| 1 | Paper ✋ |
| 2 | Scissors ✌️ |

## 📊 Win/Loss Scenarios

| Your Choice | Computer Choice | Result |
|-------------|----------------|--------|
| Rock (0) | Rock (0) | Draw |
| Rock (0) | Paper (1) | Lose |
| Rock (0) | Scissors (2) | **Win** |
| Paper (1) | Rock (0) | **Win** |
| Paper (1) | Paper (1) | Draw |
| Paper (1) | Scissors (2) | Lose |
| Scissors (2) | Rock (0) | Lose |
| Scissors (2) | Paper (1) | **Win** |
| Scissors (2) | Scissors (2) | Draw |

## 🛠️ Technical Details

- Uses `random.randint()` for computer's random choice
- Input validation with list membership check
- Efficient conditional logic handling all game scenarios
- Special case handling for rock vs scissors circular rule

### Logic Flow
1. Takes user input and validates it
2. Generates random computer choice (0-2)
3. Checks for the special case: rock beats scissors
4. Checks for draw condition
5. Compares values for remaining win/loss scenarios

## 🔮 Future Enhancements

Potential improvements for future versions:
- Add ASCII art for rock, paper, scissors
- Implement best-of-three or best-of-five rounds
- Track win/loss statistics
- Add difficulty levels (predictable vs unpredictable AI)
- Create a replay option without restarting
- Add Rock, Paper, Scissors, Lizard, Spock variant
- Include sound effects
- Add multiplayer mode (two players)
- Create a GUI version with clickable buttons
- Add animations for the countdown
- Implement tournaments with multiple rounds
- Save game history to a file
- Add different game modes (speed round, survival mode)

## 🎓 Learning Concepts

This project demonstrates:
- Random number generation
- User input handling and validation
- Conditional logic (if/elif/else)
- Comparison operators
- List membership testing
- Game state management
- Edge case handling

## 🎯 Strategy Tips

While the computer chooses randomly, here are some fun facts:
- Each choice has an equal 1/3 probability
- No pattern exists in truly random selection
- Humans tend to choose rock most often
- It's purely a game of chance!

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or additional features!

---

**Ready, Set, Shoot! 🎮**