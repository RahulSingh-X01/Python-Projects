# 🔐 Python Password Generator

A customizable password generator that creates strong, random passwords based on your specifications for letters, numbers, and symbols.

## 📖 About

This password generator helps you create secure passwords by allowing you to specify exactly how many letters, numbers, and symbols you want. It generates two versions: a simple ordered password and a shuffled version for maximum security.

## ✨ Features

- **Customizable Length**: Choose exactly how many characters of each type
- **Mixed Case Letters**: Includes both uppercase and lowercase letters (52 options)
- **Multiple Symbols**: Includes 7 different special characters
- **All Digits**: Includes numbers 0-9
- **Two Password Options**:
  - Simple password (letters → symbols → numbers order)
  - Shuffled password (randomly mixed for better security)
- **No Duplicates**: Uses `random.sample()` to ensure unique characters

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `password_generator.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the program:

```bash
python password_generator.py
```

## 💻 Example Usage

```
Welcome to the Python Password Generator!
How many letters would you like in your password?
8
How many symbols would you like?
2
How many numbers would you like?
3

simple password is:
aBcDeFgH!#123

shuffled password is:
a#1BcD!e2F3gH
```

## 🎯 Character Sets

### Letters (52 characters)
- Lowercase: a-z (26 letters)
- Uppercase: A-Z (26 letters)

### Numbers (10 characters)
- 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

### Symbols (7 characters)
- !, #, $, %, &, *, @

## 🔒 Password Strength Tips

**Strong passwords should:**
- Be at least 12-16 characters long
- Mix uppercase and lowercase letters
- Include numbers and symbols
- Be unique for each account
- Avoid dictionary words or personal information

**Recommended combinations:**
- **Basic**: 8 letters, 2 symbols, 2 numbers (12 characters)
- **Medium**: 10 letters, 3 symbols, 3 numbers (16 characters)
- **Strong**: 12 letters, 4 symbols, 4 numbers (20 characters)

## 📊 How It Works

1. **User Input**: You specify how many of each character type you want
2. **Random Selection**: The program randomly selects characters from each pool
3. **Simple Version**: Characters are combined in order (letters, symbols, numbers)
4. **Shuffled Version**: All characters are randomly mixed together
5. **Output**: Both versions are displayed for you to choose from

## 🛠️ Technical Details

- Uses `random.sample()` to prevent duplicate characters
- Uses `random.shuffle()` to randomize character order
- List concatenation to combine character types
- String `join()` method to create final password strings

## 🔮 Future Enhancements

Potential improvements for future versions:
- Add password strength meter
- Option to exclude similar-looking characters (0/O, 1/l/I)
- Copy password to clipboard automatically
- Save passwords securely to a file
- Add more symbol options
- Implement password validation rules
- Create multiple passwords at once
- Add pronounceable password option
- Include password expiry reminders
- Add option to avoid ambiguous characters
- Create a GUI version
- Add password history (securely stored)

## 🎓 Learning Concepts

This project demonstrates:
- Random number generation with `random` module
- List operations and concatenation
- String manipulation with `join()`
- User input handling with `input()`
- Type conversion with `int()`
- Random sampling without replacement
- List shuffling

## ⚠️ Security Note

This is a simple password generator for educational purposes. For production use or highly sensitive accounts, consider using:
- Dedicated password managers (LastPass, 1Password, Bitwarden)
- Two-factor authentication (2FA)
- Passphrase-based passwords for memorability

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or additional features!

---

**Stay Secure! 🛡️**