print("Welcome to the scret auction program.")


def bidding():
    name = input("What's your name?:")
    price = input("What's your bid?:$")
    auction = {name: price}
    max_bid = max(auction, key=auction.get)
    other_players = input("Are there any other bidders?\nType 'yes' or 'no':").lower()
    if other_players == "yes":
        print("\n" * 50)
        bidding()
    else:
        print("\n" * 20)
        print(f"The winner is {max_bid} with a bid of ${auction[max_bid]}")


bidding()
