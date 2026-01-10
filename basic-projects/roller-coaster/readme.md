# 🎢 Roller Coaster Ticket System

An interactive ticket pricing system for a roller coaster ride that calculates costs based on age and photo preferences!

## 📖 About

This program simulates a roller coaster ticket booth where customers can purchase tickets based on their age category. It also includes an option to add photos to their experience. The system checks height requirements and calculates the total bill automatically.

## 🎫 Pricing & Requirements

### Height Requirement
- **Minimum Height**: 120 cm
- Below 120 cm: Cannot ride

### Ticket Prices by Age
- **Child** (12 and under): $5
- **Teenage** (13-18): $7
- **Adult** (19+): $12

### Add-ons
- **Photos**: +$3 (optional)

## 🚀 How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Download or copy the `roller_coaster.py` file
3. Open your terminal/command prompt
4. Navigate to the directory containing the file
5. Run the program:

```bash
python roller_coaster.py
```

## 💻 Example Usage

### Example 1: Child Ticket with Photos
```
Welcome to the roller coaster!
Enter your Height in cm :130
You can ride the roller coaster!
Enter your age :10
Child tickets are $5.
Do you want to take pictures?
Type 'Y' for yes or 'N' for no.
Y
Your final bill is $8!
```

### Example 2: Adult Ticket without Photos
```
Welcome to the roller coaster!
Enter your Height in cm :175
You can ride the roller coaster!
Enter your age :25
Adult tickets are $12
Do you want to take pictures?
Type 'Y' for yes or 'N' for no.
N
Your final bill is $12!
```

### Example 3: Too Short to Ride
```
Welcome to the roller coaster!
Enter your Height in cm :110
Sorry!You can't ride the roller coaster.
```

### Example 4: Teenage Ticket with Photos
```
Welcome to the roller coaster!
Enter your Height in cm :160
You can ride the roller coaster!
Enter your age :16
Teenage tickets are $7.
Do you want to take pictures?
Type 'Y' for yes or 'N' for no.
Y
Your final bill is $10!
```

## ✨ Features

- **Height Validation**: Ensures riders meet minimum height requirement
- **Age-Based Pricing**: Three different ticket categories
- **Optional Add-ons**: Choice to purchase photos
- **Dynamic Billing**: Calculates total cost automatically
- **User-Friendly**: Clear prompts and pricing information

## 📊 Complete Price List

| Age Category | Base Price | With Photos | Total |
|--------------|-----------|-------------|-------|
| Child (≤12) | $5 | +$3 | $8 |
| Teenage (13-18) | $7 | +$3 | $10 |
| Adult (19+) | $12 | +$3 | $15 |

## 🎯 How It Works

1. Customer enters their height in centimeters
2. System checks if height meets minimum requirement (120 cm)
3. If eligible, customer enters their age
4. System determines ticket category and price
5. Customer chooses whether to add photos
6. System calculates and displays final bill

## 🛠️ Technical Details

- Uses integer conversion for numerical comparisons
- Nested conditional statements for age categories
- Variable accumulation for bill calculation
- Input validation through height checking
- Sequential decision-making process

## 🔮 Future Enhancements

Potential improvements for future versions:
- Add maximum height limit for safety
- Implement group discounts
- Add season passes or multi-ride tickets
- Include tax calculation
- Add more ride options with different prices
- Implement payment processing
- Add receipt printing feature
- Include date/time stamping
- Add express pass option
- Create a queue management system
- Add loyalty program points
- Include weather-based pricing
- Add family package deals
- Implement online booking system
- Create a GUI version with images

## 🎓 Learning Concepts

This project demonstrates:
- Type conversion (string to integer)
- Nested conditional statements
- Sequential decision making
- User input handling
- Variable initialization and updates
- Comparison operators
- Augmented assignment (+=)
- String formatting with f-strings

## ⚠️ Safety First!

Height requirements exist for rider safety:
- Minimum 120 cm ensures proper harness fit
- Always follow posted safety guidelines
- Supervise children on rides

## 📝 Input Format

- **Height**: Enter whole numbers in centimeters (e.g., 130)
- **Age**: Enter whole numbers (e.g., 15)
- **Photos**: Enter 'Y' for yes or 'N' for no (case-sensitive)

## 📝 License

This project is free to use and modify for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or additional features!

---

**Enjoy the Ride! 🎢**