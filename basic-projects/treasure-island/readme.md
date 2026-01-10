# 🏝️ Treasure Island Adventure Game

An interactive text-based adventure game where you make choices to find the hidden treasure while avoiding deadly traps!

## 📖 About

Welcome to Treasure Island! This is a choose-your-own-adventure style game where every decision matters. Navigate through dangerous crossroads, treacherous waters, and mysterious doors to find the legendary treasure. One wrong choice and it's game over!

## 🎮 Game Story

You arrive at Treasure Island with one mission: find the hidden treasure. Your journey will test your decision-making skills through three critical choices:

1. **The Crossroad**: Choose your path
2. **The Lake**: Decide how to cross
3. **The House**: Pick the right door

Only the wisest adventurers will survive and claim the treasure!

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `treasure_island.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the game:

```bash
python treasure_island.py
```

## 💻 Example Gameplay

### Winning Path 🏆
```
Welcome to Treasure Island!
Your mission is to find the treasure.
You're at a cross road. Where do u want to go?
Type "left" or "right"
left
You've come to a lake.There is an island in the middle of the lake.
Type "wait" to wait for boat or type "swim" to swim across.
wait
You arrived at the island unharmed.There is a house with three doors.
one red , one yellow and one blue.
Which one do you choose?
yellow
You found the treasure.
You Win!
```

### Losing Path 1 ☠️
```
Welcome to Treasure Island!
Your mission is to find the treasure.
You're at a cross road. Where do u want to go?
Type "left" or "right"
right
You've fallen into a hole.
Game over!
```

### Losing Path 2 ☠️
```
You're at a cross road. Where do u want to go?
Type "left" or "right"
left
You've come to a lake.There is an island in the middle of the lake.
Type "wait" to wait for boat or type "swim" to swim across.
swim
You've been attacked by a trout.
Game over!
```

### Losing Path 3 ☠️
```
[After choosing left and wait...]
You arrived at the island unharmed.There is a house with three doors.
one red , one yellow and one blue.
Which one do you choose?
red
You've been burned by fire.
Game over!
```

## 🗺️ Decision Tree

```
START: Treasure Island
    |
    ├─ RIGHT ➜ Fall into hole ☠️ GAME OVER
    |
    └─ LEFT ➜ Lake
           |
           ├─ SWIM ➜ Attacked by trout ☠️ GAME OVER
           |
           └─ WAIT ➜ Island with 3 Doors
                  |
                  ├─ RED ➜ Burned by fire ☠️ GAME OVER
                  ├─ BLUE ➜ Eaten by beasts ☠️ GAME OVER
                  └─ YELLOW ➜ Found treasure! 🏆 YOU WIN!
```

## ✨ Features

- **Multiple Choice Paths**: 3 decision points
- **Multiple Endings**: 4 different game over scenarios + 1 winning path
- **Story-Driven**: Engaging narrative with consequences
- **Simple Commands**: Easy text-based input
- **Instant Feedback**: Immediate results for each choice

## 🎯 Winning Strategy

**The correct path to treasure:**
1. Choose **"left"** at the crossroad
2. Choose **"wait"** at the lake
3. Choose **"yellow"** door at the house

**Remember**: Patience and caution are rewarded in this adventure!

## 📊 Game Statistics

- **Total Possible Paths**: 8
- **Winning Paths**: 1 (12.5% success rate)
- **Losing Paths**: 4 (50% if you reach final choice)
- **Decision Points**: 3
- **Difficulty**: Medium

## 🛠️ Technical Details

- Uses nested if-else statements for branching storylines
- String comparison for user input validation
- Multi-line strings for narrative text
- Sequential decision-making structure
- Binary choices at each decision point

## 🔮 Future Enhancements

Potential improvements for future versions:
- Add more decision points and paths
- Include inventory system
- Add character stats (health, courage, etc.)
- Implement random encounters
- Add sound effects
- Create save/load game feature
- Add achievements system
- Include multiple difficulty levels
- Add time-based challenges
- Create ASCII art for scenes
- Implement puzzle-solving elements
- Add companions or NPCs
- Create branching storylines with multiple endings
- Add a scoring system
- Include Easter eggs and secrets
- Create a map system

## 🎓 Learning Concepts

This project demonstrates:
- Conditional logic (if/elif/else)
- Nested conditional statements
- User input handling
- String comparison
- Game state management
- Branching narratives
- Multi-line strings with triple quotes
- Sequential program flow

## 📝 Input Format

All inputs are **case-sensitive strings**:
- Crossroad: `"left"` or `"right"`
- Lake: `"wait"` or `"swim"`
- Doors: `"red"`, `"blue"`, or `"yellow"`

**Tip**: Make sure to type exactly as shown (lowercase)!

## 🎭 Game Over Scenarios

1. **Fall into a hole** - Choosing right at crossroad
2. **Attacked by trout** - Choosing to swim across lake
3. **Burned by fire** - Choosing red door
4. **Eaten by beasts** - Choosing blue door

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and add your own adventure paths, puzzles, or story elements!

---

**Good Luck on Your Adventure! 🗺️💎**