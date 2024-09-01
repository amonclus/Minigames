import random

# Define the card deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Create a deck of cards
def create_deck():
    deck = [{'suit': suit, 'rank': rank, 'value': values[rank]} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Calculate the value of a hand
def calculate_hand_value(hand):
    value = sum(card['value'] for card in hand)
    # Adjust for Aces
    aces = sum(1 for card in hand if card['rank'] == 'Ace')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Display the hand
def display_hand(hand, name):
    cards = [f"{card['rank']} of {card['suit']}" for card in hand]
    print(f"{name} hand: {', '.join(cards)}")

# Main game loop
def blackjack():
    deck = create_deck()

    # Initial deal
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Player's turn
    while True:
        display_hand(player_hand, "Player")
        player_value = calculate_hand_value(player_hand)
        print(f"Player's hand value: {player_value}")

        if player_value > 21:
            print("Player busts! Dealer wins.")
            return
        elif player_value == 21:
            print("Blackjack! Player wins.")
            return

        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deal_card(deck))
        elif action == 'stand':
            break
        else:
            print("Invalid input, please choose 'hit' or 'stand'.")

    # Dealer's turn
    while True:
        display_hand(dealer_hand, "Dealer")
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Dealer's hand value: {dealer_value}")

        if dealer_value > 21:
            print("Dealer busts! Player wins.")
            return
        elif dealer_value >= 17:
            break
        else:
            print("Dealer hits.")
            dealer_hand.append(deal_card(deck))

    # Determine winner
    if player_value > dealer_value:
        print("Player wins!")
    elif dealer_value > player_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    blackjack()
