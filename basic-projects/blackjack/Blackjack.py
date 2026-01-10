import random

print("Welcome to the BLACKJACK.")


def blackjack():
    while True:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        random.shuffle(cards)
        player_hand = []
        dealer_hand = []
        player_score = 0
        dealer_score = 0
        
        start = input("Do u want to play a game of Blackjack? Type 'y' or 'n': ")
        if start == "n":
            print("Thanks for playing.\nGood Bye!")
            break
        else:
            card_1 = cards.pop()
            card_2 = cards.pop()
            card_3 = cards.pop()
            card_4 = cards.pop()
            player_hand = [card_1, card_2]
            dealer_hand = [card_3, card_4]
            
            print(f"Your cards : {player_hand}")
            print(f"Dealer's card : {dealer_hand[0]}")
            
            player_score = sum(player_hand)
            dealer_score = sum(dealer_hand)
            
            # Handle Ace in player's initial hand
            if player_score > 21 and 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
                player_score = sum(player_hand)
            
            print(f"Your current score : {player_score}")
            
            if player_score == 21:
                print("You have a Blackjack!\nYou Won.")
                continue
            if dealer_score == 21:
                print(f"Dealer's cards = {dealer_hand}")
                print(f"Dealer's score = {dealer_score}")
                print("Dealer have a Blackjack!\nYou lose.")
                continue
            
            game_over = False
            while not game_over:
                another_card = input(
                    "Type 'y' to get another card or type 'n' to pass. : "
                )
                if another_card == "y":
                    new_card = cards.pop()
                    player_hand.append(new_card)
                    player_score = sum(player_hand)
                    
                    # Handle Ace when player draws
                    if player_score > 21 and 11 in player_hand:
                        player_hand[player_hand.index(11)] = 1
                        player_score = sum(player_hand)
                    
                    print(f"Player's cards : {player_hand}")
                    print(f"Your current score : {player_score}")
                    
                    if player_score > 21:
                        print(f"Dealer's cards = {dealer_hand}")
                        print(f"Dealer's score = {dealer_score}")
                        print("You went over.\nYou lose.")
                        game_over = True
                else:
                    while dealer_score < 17:
                        new_dealer_card = cards.pop()
                        dealer_hand.append(new_dealer_card)
                        dealer_score = sum(dealer_hand)
                        
                        # Handle Ace for dealer
                        if dealer_score > 21 and 11 in dealer_hand:
                            dealer_hand[dealer_hand.index(11)] = 1
                            dealer_score = sum(dealer_hand)
                    
                    print(f"Dealer's cards : {dealer_hand}")
                    print(f"Dealer's score : {dealer_score}")
                    
                    if dealer_score > 21:
                        print("Dealer went over.\nYou win!")
                        game_over = True
                    elif player_score > dealer_score:
                        print("You win!")
                        game_over = True
                    elif player_score == dealer_score:
                        print("It's a draw!")
                        game_over = True
                    else:
                        print("You lose!")
                        game_over = True


blackjack()
