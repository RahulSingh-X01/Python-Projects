print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do u want?'S','M','L'\n")
pepperoni = input("Do u want pepperoni on your pizza?'Y'or'N'\n")
extra_cheese = input("Do u want extra cheese?'Y'or'N'\n")
bill = 0

if size == "S":
    print("Price of small size pizza is $15")
    bill = 15
elif size == "M":
    print("Price of medium size pizza is $20")
    bill = 20
else:
    print("Price of large size pizza is $25")
    bill = 25

if pepperoni == "Y":
    if size == "S":
        print("Price for pepperoni for small pizza is $2")
        bill += 2
    else:
        print("Price for pepperoni for medium or large pizza is $3")
        bill += 3

else:
    print("No pepperoni added.")

if extra_cheese == "Y":
    print("Price for extra cheese is $1")
    bill += 1

else:
    print("No extra cheese added.")

print(f"Your final bill is ${bill}")
