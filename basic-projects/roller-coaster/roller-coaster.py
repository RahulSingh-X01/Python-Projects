print("Welcome to the roller coaster!")
height = int(input("Enter your Height in cm :"))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Enter your age :"))
    
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Teenage tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12")
        bill = 12
    want_photos = input("Do you want to take pictures?\nType 'Y' for yes or 'N' for no.\n")
    if want_photos == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}!")
else:
    print("Sorry!You can't ride the roller coaster.")