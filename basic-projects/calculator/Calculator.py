def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculation():
    should_continue = True
    
    while should_continue:
        num_1 = float(input("What's the first number?: "))
        continuation = True
        
        while continuation:
            for symbol in operation:
                print(symbol)
            symbols = input("Pick an operation: ")
            num_2 = float(input("What's the second number?: "))
            
            answer = operation[symbols](num_1, num_2)
            print(f"{num_1} {symbols} {num_2} = {answer}")
            
            choice = input(
                "Type 'y' for continuing calculation with the result or type 'n' for starting new calculation.: "
            ).lower()
            if choice == "y":
                num_1 = answer
            else:
                continuation = False
                print("\n" * 20)


calculation()
