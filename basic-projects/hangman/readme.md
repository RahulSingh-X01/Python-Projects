# 🎭 Hangman Game

A classic word-guessing game where you try to guess a random word one letter at a time before the hangman is complete!

## 📖 About

Hangman is a timeless word puzzle game. The computer selects a random word, and you must guess it letter by letter. Each wrong guess adds a part to the hangman drawing. Guess the word before the drawing is complete to win!

## 🎮 Game Rules

- The computer randomly selects a word from a predefined list
- You see blanks representing each letter in the word
- Guess one letter at a time
- **Correct guess**: The letter is revealed in all positions where it appears
- **Wrong guess**: You lose one life and a body part is added to the hangman
- **You have 7 lives** (7 wrong guesses allowed)
- **Win** by guessing all letters before running out of lives
- **Lose** if the hangman drawing is completed (0 lives left)

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `hangman.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the game:

```bash
python hangman.py
```

## 💻 Example Gameplay

### Winning Game
```
apple
_ _ _ _ _
Guess a letter : a
Current word: a_ _ _ _
Guess a letter : e
Current word: a_ _ _ e
Guess a letter : p
Current word: app_ e
Guess a letter : l
Current word: apple
You win!
```

### Losing Game
```
elephant
_ _ _ _ _ _ _ _
Guess a letter : a
Current word: _ _ _ _ _ a _ _
Guess a letter : z

Incorrect word
Lives left : 6
	
  +---+
  |   |
  O   |
      |
      |
      |
=========
Current word: _ _ _ _ _ a _ _
[... more wrong guesses ...]
You lose
The actual word is elephant
```

## ✨ Features

- **Visual Hangman Drawing**: ASCII art that builds with each wrong guess
- **Word Variety**: 13 different words of varying difficulty
- **Lives Counter**: Track how many attempts you have left
- **Progressive Reveal**: See the word being filled in as you guess correctly
- **Clear Win/Loss Conditions**: Know exactly when the game ends

## 📋 Word List

The game includes these words:
- apple, chair, house, book, bicycle
- kitchen, garden, astronaut, hypothesis
- elephant, pyramid, compass, rainbow

## 🎯 Strategy Tips

1. **Start with vowels**: a, e, i, o, u appear in most words
2. **Common consonants**: Try r, s, t, n, l next
3. **Look for patterns**: Notice word length and revealed letters
4. **Avoid rare letters**: Save q, x, z for later unless you're sure
5. **Think of common words**: Use the word length as a clue

## 📊 Hangman Stages

The game has 7 stages (lives):
1. Empty gallows
2. Head
3. Body
4. Left arm
5. Right arm
6. Left leg
7. Right leg (Game Over!)

## 🔮 Future Enhancements

Potential improvements for future versions:
- Add difficulty levels (easy/medium/hard words)
- Expand word list with categories (animals, countries, foods)
- Track guessed letters to avoid duplicates
- Add score system based on remaining lives
- Implement replay option
- Add multiplayer mode (player vs player)
- Create a hints system
- Add word definitions after game ends
- Save high scores and statistics
- Create a GUI version with graphics

## 🛠️ Technical Details

- Uses Python's `random` module for word selection
- Stores hangman stages as ASCII art in a list
- List comprehension for creating blank spaces
- String manipulation for revealing letters
- While loop with game state management

## 🎓 Learning Concepts

This project demonstrates:
- Random selection with `random.sample()`
- List manipulation and iteration
- String operations (join, indexing)
- ASCII art and multi-line strings
- Game loop logic
- Conditional statements
- User input handling

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or additional features!

---

**Good Luck and Happy Guessing! 🎉**