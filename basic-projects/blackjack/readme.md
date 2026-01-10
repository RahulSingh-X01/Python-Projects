# 🎰 Blackjack Game

A simple command-line implementation of the classic Blackjack card game built with Python.

## 📖 About

This is a text-based Blackjack game where you play against a computer dealer. The goal is to get as close to 21 as possible without going over, while having a higher score than the dealer.

## 🎮 Game Rules

- The game uses a standard deck with cards valued as follows:
  - Number cards (2-10): Face value
  - Face cards (Jack, Queen, King): 10 points
  - Ace: 11 points
  - Both player and dealer start with 2 cards
  - Player can see one of the dealer's cards
  - Player can choose to "hit" (draw another card) or "stand" (keep current hand)
  - If player's score exceeds 21, they bust and lose
  - Dealer must hit until their score is at least 17
  - Highest score under or equal to 21 wins

### Winning Conditions

- **Blackjack**: Getting 21 with your first two cards (automatic win)
- **Beat the Dealer**: Having a higher score than the dealer without busting
- **Dealer Busts**: Dealer goes over 21 while you're still in the game
- **Draw**: Both player and dealer have the same score

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `blackjack.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the game:

```bash
python blackjack.py
```

## 🎯 How to Play

1. When prompted, type `y` to start a new game or `n` to exit
2. You'll see your two cards and one of the dealer's cards
3. Decide whether to hit (`y`) or stand (`n`)
4. If you choose to hit, you'll receive another card
5. Continue hitting or stand when you're satisfied with your hand
6. The dealer will then play their hand automatically
7. The winner is determined and displayed

## 💻 Example Gameplay

```
Welcome to the BLACKJACK.
Do u want to play a game of Blackjack? Type 'y' or 'n': y
Your cards : [10, 8]
Dealer's card : 7
Your current score : 18
Type 'y' to get another card or type 'n' to pass. : n
Dealer's cards : [7, 9]
Dealer's score : 16
You win!
```

## 🛠️ Features

- Randomized card dealing from a 52-card deck
- Automatic Blackjack detection
- Dealer AI that follows standard casino rules (hits until 17)
- Continuous play option
- Clear score tracking

## 📋 Requirements

- Python 3.x
- No external libraries required (uses only standard library)

## 🔮 Future Enhancements

Potential improvements for future versions:
- Implement proper Ace handling (1 or 11 points based on hand)
- Add betting system with virtual chips
- Track win/loss statistics
- Support for multiple players
- Add splitting and doubling down options
- Create a graphical user interface (GUI)

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes!

---

**Enjoy the game and may the odds be in your favor! 🎲**