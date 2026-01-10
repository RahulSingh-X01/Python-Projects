# 🍕 Python Pizza Deliveries

A simple command-line pizza ordering system where customers can customize their pizza and get an instant price calculation!

## 📖 About

This is an interactive pizza ordering program that calculates the total cost based on the size of pizza and selected toppings. Perfect for learning conditional logic and basic billing systems in Python!

## 🍕 Menu & Pricing

### Pizza Sizes
- **Small (S)**: $15
- **Medium (M)**: $20
- **Large (L)**: $25

### Toppings
- **Pepperoni**:
  - Small pizza: +$2
  - Medium/Large pizza: +$3
- **Extra Cheese**: +$1 (all sizes)

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `pizza_order.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the program:

```bash
python pizza_order.py
```

## 💻 Example Usage

### Example 1: Small Pizza with All Toppings
```
Welcome to the Python Pizza Deliveries!
What size pizza do u want?'S','M','L'
S
Do u want pepperoni on your pizza?'Y'or'N'
Y
Do u want extra cheese?'Y'or'N'
Y
Price of small size pizza is $15
Price for pepperoni for small pizza is $2
Price for extra cheese is $1
Your final bill is $18
```

### Example 2: Large Pizza, No Toppings
```
Welcome to the Python Pizza Deliveries!
What size pizza do u want?'S','M','L'
L
Do u want pepperoni on your pizza?'Y'or'N'
N
Do u want extra cheese?'Y'or'N'
N
Price of large size pizza is $25
No pepperoni added.
No extra cheese added.
Your final bill is $25
```

### Example 3: Medium Pizza with Pepperoni
```
Welcome to the Python Pizza Deliveries!
What size pizza do u want?'S','M','L'
M
Do u want pepperoni on your pizza?'Y'or'N'
Y
Do u want extra cheese?'Y'or'N'
N
Price of medium size pizza is $20
Price for pepperoni for medium or large pizza is $3
No extra cheese added.
Your final bill is $23
```

## ✨ Features

- **Three Size Options**: Small, Medium, or Large
- **Customizable Toppings**: Add pepperoni and/or extra cheese
- **Dynamic Pricing**: Pepperoni price varies by pizza size
- **Transparent Billing**: Shows itemized costs as you order
- **Final Total**: Clear display of your total bill at the end

## 🎯 How It Works

1. Customer selects pizza size (S/M/L)
2. Customer chooses whether to add pepperoni (Y/N)
3. Customer chooses whether to add extra cheese (Y/N)
4. Program calculates base price based on size
5. Program adds topping costs based on selections
6. Final bill is displayed with complete breakdown

## 📊 Price Breakdown Examples

| Size | Base | + Pepperoni | + Extra Cheese | Total |
|------|------|-------------|----------------|-------|
| Small | $15 | +$2 | +$1 | $18 |
| Medium | $20 | +$3 | +$1 | $24 |
| Large | $25 | +$3 | +$1 | $29 |

## 🛠️ Technical Details

- Uses nested if-elif-else statements for decision making
- Variable accumulation for bill calculation
- String input handling with uppercase letters
- Progressive bill updates with += operator
- Clear, step-by-step output for transparency

## 🔮 Future Enhancements

Potential improvements for future versions:
- Add more toppings (mushrooms, olives, onions, etc.)
- Implement crust options (thin, thick, stuffed)
- Add drink and side options
- Multiple pizza orders in one session
- Apply discounts or coupon codes
- Save orders to a file
- Add delivery fee calculation
- Implement tax calculation
- Create a receipt format
- Add order confirmation number
- Support for half-and-half pizzas
- Add vegetarian/vegan options
- Implement combo deals
- Create a GUI version

## 🎓 Learning Concepts

This project demonstrates:
- Conditional statements (if/elif/else)
- Nested conditionals
- Variable initialization and updates
- User input handling
- String comparison
- Basic arithmetic operations
- Augmented assignment operators (+=)
- F-string formatting

## 📝 Input Format

- **Size**: Enter 'S', 'M', or 'L' (case-sensitive)
- **Pepperoni**: Enter 'Y' for yes or 'N' for no
- **Extra Cheese**: Enter 'Y' for yes or 'N' for no

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or additional features!

---

**Enjoy Your Pizza! 🍕**