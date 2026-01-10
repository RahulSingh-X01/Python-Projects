import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "*", "@"]

print("Welcome to the Python Password Generator!")

letters_used = int(input("How many letters would you like in your password?\n"))
symbols_used = int(input("How many symbols would you like?\n"))
numbers_used = int(input("How many numbers would you like?\n"))

letters_chosen = random.sample(letters, letters_used)
symbols_chosen = random.sample(symbols, symbols_used)
numbers_chosen = random.sample(numbers, numbers_used)

password = letters_chosen + symbols_chosen + numbers_chosen

simple_password = "".join(password)

print(f"simple password is:\n{simple_password}")

random.shuffle(password)

suffled_password = "".join(password)

print(f"shuffled password is:\n{suffled_password}")
