# 🧮 Simple Calculator

A command-line calculator that performs basic arithmetic operations with the ability to chain calculations using previous results.

## 📖 About

This is an interactive calculator program that allows you to perform basic mathematical operations (addition, subtraction, multiplication, and division). The unique feature is that you can continue calculating with the result of your previous operation, making it perfect for complex multi-step calculations.

## ✨ Features

- **Four Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Chained Calculations**: Continue calculating with your previous result
- **Error Handling**: Prevents division by zero and invalid operations
- **User-Friendly**: Clear prompts and formatted output
- **Continuous Use**: Start new calculations without restarting the program

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `calculator.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the program:

```bash
python calculator.py
```

## 💻 Example Usage

### Simple Calculation
```
What's the first number?: 10
+
-
*
/
Pick an operation: +
What's the second number?: 5
10.0 + 5.0 = 15.0
Type 'y' for continuing calculation with the result or type 'n' for starting new calculation.: n
```

### Chained Calculation
```
What's the first number?: 100
+
-
*
/
Pick an operation: -
What's the second number?: 25
100.0 - 25.0 = 75.0
Type 'y' for continuing calculation with the result or type 'n' for starting new calculation.: y
+
-
*
/
Pick an operation: *
What's the second number?: 2
75.0 * 2.0 = 150.0
Type 'y' for continuing calculation with the result or type 'n' for starting new calculation.: y
+
-
*
/
Pick an operation: /
What's the second number?: 3
150.0 / 3.0 = 50.0
```

## 🎯 How It Works

1. Enter your first number
2. Choose an operation from the displayed symbols (+, -, *, /)
3. Enter your second number
4. View the result
5. Choose to either:
   - Continue calculating with the result (type 'y')
   - Start a fresh calculation (type 'n')

## 📋 Requirements

- Python 3.x
- No external libraries required (uses only standard library)

## 🛡️ Error Handling

The calculator includes protection against:
- **Division by zero**: Returns an error message instead of crashing
- **Invalid operations**: Prompts you to choose a valid operation
- **Decimal numbers**: Supports both integers and floating-point numbers

## 🔮 Future Enhancements

Potential improvements for future versions:
- Add more operations (power, square root, modulo, etc.)
- Implement order of operations for complex expressions
- Add calculation history feature
- Save and load previous calculations
- Add memory functions (M+, M-, MR, MC)
- Support for parentheses in expressions
- Create a GUI version with buttons
- Add scientific calculator functions
- Export calculation results to a file

## 🛠️ Technical Details

- Uses Python dictionaries to map operation symbols to functions
- Implements higher-order functions (functions as dictionary values)
- Floating-point arithmetic for decimal support
- Clean code structure with separate functions for each operation
- Nested loops for continuous operation

## 🎓 Learning Concepts

This project demonstrates:
- Function definitions and calls
- Dictionary usage with function values
- While loops and control flow
- User input handling
- String formatting
- Error handling and validation

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or additional features!

---

**Happy Calculating! ✨**